import asyncio
import base64
import json
import logging
import os

import requests
import websockets
from websockets.exceptions import ConnectionClosedError

from ai_cloud_sdk_4pd import models as ai_cloud_sdk_4pd_models


class Client:
    def __init__(
        self,
        config: ai_cloud_sdk_4pd_models.Config,
    ):
        self._token = config.token
        self._call_token = config.call_token
        # self._endpoint = config.endpoint
        self._region = config.region
        self._http_endpoint = None
        self._websocket_endpoint = None
        self.blacklist_token = []
        self.blacklist_call_token = []

        # asr websocket
        self._ws_asr = None

        # 设置region和endpoint
        self._http_endpoint_map = {
            'China': 'http://172.26.1.45:8202',
            # 'China': 'localhost:8090/ai/cpp/api',
            'HongKong': 'https://Hongkong.com',
            'Other': 'https://Other.com',
        }
        self._websocket_endpoint_map = {
            'China': 'ws://172.26.1.45:8090',
            # 'China': 'ws://localhost:8090',
            # 'HongKong': 'https://Hongkong.com',
            # 'Other': 'https://Other.com',
        }
        self.__set_region_and_endpoint()
        self.__verify_tokens()

    def __set_region_and_endpoint(self) -> None:
        # 如果endpoint已给出且合法，则直接返回
        # if self._endpoint and self._endpoint in self._endpoint_map.values():
        #     self._region = [
        #         k for k, v in self._endpoint_map.items() if v == self._endpoint
        #     ][0]
        #     return

        # 如果endpoint未给出或不合法，且region存在且合法，则根据region确定endpoint
        if (
            self._region
            and self._region in self._http_endpoint_map.keys()
            and self._region in self._websocket_endpoint_map.keys()
        ):
            self._http_endpoint = self._http_endpoint_map[self._region]
            self._websocket_endpoint = self._websocket_endpoint_map[self._region]
            return

        # 如果endpoint未给出或不合法，且region不存在或不合法，则默认endpoint(China)
        self._region = 'China'
        self._http_endpoint = self._http_endpoint_map[self._region]
        self._websocket_endpoint = self._websocket_endpoint_map[self._region]
        return

    def __verify_tokens(self) -> None:
        # 如果token或call_token未给出，则抛出异常
        if self._token is None or self._call_token is None:
            raise ValueError('token and call_token is required')

    def audio_language_detection(
        self,
        request: ai_cloud_sdk_4pd_models.BaseRequest = None,
    ) -> ai_cloud_sdk_4pd_models.BaseResponse:

        # 如果token或call_token在黑名单中，则抛出异常
        if (
            self._token in self.blacklist_token
            or self._call_token in self.blacklist_call_token
        ):
            raise ValueError('token or call_token is forbidden to send request')

        full_url = f'{self._http_endpoint}{request.api}'
        headers = {
            'token': self._token,
            'call_token': self._call_token,
            'content-type': request.content_type,
        }

        headers = {
            'token': self._token,
            'call_token': self._call_token,
        }
        payload = request.payload
        file_url = payload.get('audio')
        metadata = payload.get('metadata')
        choices = payload.get('choices')
        files = {'audio': (file_url, open(file_url, 'rb'))}
        response = requests.request(
            method=request.method,
            url=full_url,
            headers=headers,
            data={'metadata': metadata, 'choices': choices},
            files=files,
        )

        # 如果返回码为503，则将token和call_token加入黑名单
        if response.json().get('code', None) == 503:
            self.blacklist_token.append(self._token)
            self.blacklist_call_token.append(self._call_token)
            raise ValueError('token or call_token is invalid')

        return ai_cloud_sdk_4pd_models.BaseResponse(
            code=response.json().get('code', None),
            data=response.json().get('data', None),
            message=response.json().get('message', None),
        )

    async def _asr_send_data(self, request, websocket):
        file_url = request.audio_url
        try:
            with open(file_url, 'rb') as f:
                audio_data = f.read()
                audio_base64 = base64.b64encode(audio_data)
                audio_base64 = audio_base64.decode('utf-8')
        except FileNotFoundError:
            raise ValueError('File not found. Please check the path and try again.')

        # 发送音频数据
        message = {
            "enableWords": True,
            "lang": request.language,
            "waitTime": 500,
            "chunkSize": 1024,
            "fileBase64": audio_base64,
            "finalResult": 'true' if request.final_result else 'false',
        }

        if (
            self._token in self.blacklist_token
            or self._call_token in self.blacklist_call_token
        ):
            raise ValueError('token or call_token is forbidden to send request')
        await websocket.send(json.dumps(message))

    async def _asr_receive_data(
        self,
        request,
        websocket,
        on_ready,
        on_response,
        on_completed,
    ):
        try:
            flag = False
            while websocket.open:
                if (
                    self._token in self.blacklist_token
                    or self._call_token in self.blacklist_call_token
                ):
                    raise ValueError('token or call_token is forbidden to send request')

                try:
                    if flag:
                        recv_data = await asyncio.wait_for(
                            websocket.recv(), timeout=request.timeout
                        )
                    else:
                        recv_data = await websocket.recv()
                except asyncio.TimeoutError:
                    await on_completed()
                    logging.info('service completed with timeout')
                    break

                if isinstance(recv_data, str):
                    recv_data = str(recv_data)
                    recv_data = json.loads(recv_data)
                    print(recv_data)

                    if recv_data.get('success', False):
                        await on_ready()
                        flag = True
                        continue

                    if recv_data.get('code', None) == 503:
                        self.blacklist_token.append(self._token)
                        self.blacklist_call_token.append(self._call_token)
                        raise ValueError('token or call_token is invalid')

                    if recv_data.get('end', False):
                        await on_completed()
                        break

                    await on_response(recv_data)

                else:
                    raise Exception("Received data is not str")
        except ConnectionClosedError as e:
            logging.error('ConnectionClosedError')
            # raise e
        except Exception as e:
            raise e
        logging.info('service completed')

    async def asr(
        self,
        request: ai_cloud_sdk_4pd_models.ASRRequest = None,
        on_ready: callable = None,
        on_response: callable = None,
        on_completed: callable = None,
    ) -> None:

        if (
            self._token in self.blacklist_token
            or self._call_token in self.blacklist_call_token
        ):
            raise ValueError('token or call_token is forbidden to send request')

        full_url = f"{self._websocket_endpoint}{request.api}"
        headers = {
            'token': self._token,
            'call_token': self._call_token,
        }
        # print(full_url)
        async with websockets.connect(
            full_url,
            extra_headers=headers,
            ping_timeout=60,
            ping_interval=60,
            close_timeout=60,
        ) as websocket:
            # 创建并发任务：一个发送数据，一个接收数据
            send_task = asyncio.create_task(self._asr_send_data(request, websocket))
            receive_task = asyncio.create_task(
                self._asr_receive_data(
                    request,
                    websocket,
                    on_ready,
                    on_response,
                    on_completed,
                )
            )

            # 等待发送任务完成
            await send_task
            # 等待接收任务完成
            await receive_task
        # # 设置 ping 的超时时间和 ping 的间隔
        # ping_timeout = 120  # 秒
        # ping_interval = 60  # 秒
        # close_timeout = 60  # 当尝试关闭连接时，等待关闭帧的最长时间（秒）
        # if self._ws_asr is None:
        #     self._ws_asr = await websockets.connect(
        #         full_url,
        #         extra_headers=headers,
        #         ping_timeout=ping_timeout,
        #         ping_interval=ping_interval,
        #         close_timeout=close_timeout,
        #     )
        # try:
        #     if self._ws_asr.open is not True:
        #         self._ws_asr = await websockets.connect(
        #             full_url,
        #             extra_headers=headers,
        #             ping_timeout=ping_timeout,
        #             ping_interval=ping_interval,
        #             close_timeout=close_timeout,
        #         )
        # except Exception as e:
        #     raise e

        # # 创建并发任务：一个发送数据，一个接收数据
        # send_task = asyncio.create_task(self._asr_send_data(request))
        # receive_task = asyncio.create_task(
        #     self._asr_receive_data(
        #         request,
        #         on_ready,
        #         on_response,
        #         on_completed,
        #     )
        # )
        #
        # # 等待发送任务完成
        # await send_task
        # # 等待接收任务完成
        # await receive_task
        #  把wav文件进行base64编码
        # file_url = request.audio_url
        # try:
        #     with open(file_url, 'rb') as f:
        #         audio_data = f.read()
        #         audio_base64 = base64.b64encode(audio_data)
        #         audio_base64 = audio_base64.decode('utf-8')
        # except FileNotFoundError:
        #     raise ValueError('File not found. Please check the path and try again.')
        #
        # # 发送音频数据
        # message = {
        #     "enableWords": True,
        #     "lang": request.language,
        #     "waitTime": 5,
        #     "chunkSize": 1024,
        #     "fileBase64": audio_base64,
        #     "finalResult": 'true' if request.final_result else 'false',
        # }
        #
        # if (
        #     self._token in self.blacklist_token
        #     or self._call_token in self.blacklist_call_token
        # ):
        #     raise ValueError('token or call_token is forbidden to send request')
        # await self._ws_asr.send(json.dumps(message))

        # 4. 接收返回数据
        # try:
        #     flag = False
        #     while self._ws_asr.open:
        #         if (
        #             self._token in self.blacklist_token
        #             or self._call_token in self.blacklist_call_token
        #         ):
        #             raise ValueError('token or call_token is forbidden to send request')
        #
        #         try:
        #             if flag:
        #                 recv_data = await asyncio.wait_for(
        #                     self._ws_asr.recv(), timeout=request.timeout
        #                 )
        #             else:
        #                 recv_data = await self._ws_asr.recv()
        #         except asyncio.TimeoutError:
        #             await on_completed()
        #             logging.info('service completed with timeout')
        #             break
        #
        #         if isinstance(recv_data, str):
        #             recv_data = str(recv_data)
        #             recv_data = json.loads(recv_data)
        #
        #             if recv_data.get('success', False):
        #                 await on_ready()
        #                 flag = True
        #                 continue
        #
        #             if recv_data.get('code', None) == 503:
        #                 self.blacklist_token.append(self._token)
        #                 self.blacklist_call_token.append(self._call_token)
        #                 raise ValueError('token or call_token is invalid')
        #
        #             if recv_data.get('end', False):
        #                 await on_completed()
        #                 break
        #
        #             await on_response(recv_data)
        #
        #         else:
        #             raise Exception("Received data is not str")
        # except ConnectionClosedError as e:
        #     logging.error('ConnectionClosedError')
        #     # raise e
        # except Exception as e:
        #     raise e
        # logging.info('service completed')

    def translate_text(
        self,
        request: ai_cloud_sdk_4pd_models.BaseRequest = None,
    ) -> ai_cloud_sdk_4pd_models.BaseResponse:

        # 如果token或call_token在黑名单中，则抛出异常
        if (
            self._token in self.blacklist_token
            or self._call_token in self.blacklist_call_token
        ):
            raise ValueError('token or call_token is forbidden to send request')

        full_url = f'{self._http_endpoint}{request.api}'
        headers = {
            'token': self._token,
            'call_token': self._call_token,
            'content-type': request.content_type,
        }

        payload = request.payload

        response = requests.request(
            method=request.method,
            url=full_url,
            headers=headers,
            data=json.dumps(payload),
        )

        # 如果返回码为503，则将token和call_token加入黑名单
        if response.json().get('code', None) == 503:
            self.blacklist_token.append(self._token)
            self.blacklist_call_token.append(self._call_token)
            raise ValueError('token or call_token is invalid')

        return ai_cloud_sdk_4pd_models.BaseResponse(
            code=response.json().get('code', None),
            data=response.json().get('data', None),
            message=response.json().get('message', None),
        )

    def tts(
        self,
        request: ai_cloud_sdk_4pd_models.BaseRequest = None,
    ):

        # 如果token或call_token在黑名单中，则抛出异常
        if (
            self._token in self.blacklist_token
            or self._call_token in self.blacklist_call_token
        ):
            raise ValueError('token or call_token is forbidden to send request')

        full_url = f'{self._http_endpoint}{request.api}'
        headers = {
            'token': self._token,
            'call_token': self._call_token,
            'content-type': request.content_type,
        }

        payload = request.payload

        response = requests.request(
            method=request.method,
            url=full_url,
            headers=headers,
            data=json.dumps(payload),
        )

        return response
        #
        # # 如果返回码为503，则将token和call_token加入黑名单
        # if response.json().get('code', None) == 503:
        #     self.blacklist_token.append(self._token)
        #     self.blacklist_call_token.append(self._call_token)
        #     raise ValueError('token or call_token is invalid')
        #
        # return ai_cloud_sdk_4pd_models.BaseResponse(
        #     code=response.json().get('code', None),
        #     data=response.json().get('data', None),
        #     message=response.json().get('message', None),
        # )

    async def asr_batch(
        self,
        request: ai_cloud_sdk_4pd_models.ASRRequest = None,
        on_ready: callable = None,
        on_response: callable = None,
        on_completed: callable = None,
    ) -> None:

        if (
            self._token in self.blacklist_token
            or self._call_token in self.blacklist_call_token
        ):
            raise ValueError('token or call_token is forbidden to send request')

        full_url = f"{self._websocket_endpoint}{request.api}"
        headers = {
            'token': self._token,
            'call_token': self._call_token,
        }

        directory_path = request.batch_directory
        if not directory_path:
            raise ValueError('batch_directory is required')

        # 设置 ping 的超时时间和 ping 的间隔
        ping_timeout = 120  # 秒
        ping_interval = 5  # 秒
        close_timeout = 60  # 当尝试关闭连接时，等待关闭帧的最长时间（秒）
        if self._ws_asr is None:
            self._ws_asr = await websockets.connect(
                full_url,
                extra_headers=headers,
                ping_timeout=ping_timeout,
                ping_interval=ping_interval,
                close_timeout=close_timeout,
            )
        if not self._ws_asr.open:
            self._ws_asr = await websockets.connect(
                full_url,
                extra_headers=headers,
                ping_timeout=ping_timeout,
                ping_interval=ping_interval,
                close_timeout=close_timeout,
            )

        # 读取目录下的所有文件，筛选出wav文件
        files = os.listdir(directory_path)
        wav_files = []
        for file in files:
            if file.endswith('.wav'):
                wav_files.append(file)

        # 把wav文件进行base64编码
        for file in wav_files:
            file_url = os.path.join(directory_path, file)

            try:
                with open(file_url, 'rb') as f:
                    audio_data = f.read()
                    audio_base64 = base64.b64encode(audio_data)
                    audio_base64 = audio_base64.decode('utf-8')
            except FileNotFoundError:
                raise ValueError('File not found. Please check the path and try again.')

            # 发送音频数据
            message = {
                "enableWords": True,
                "lang": request.language,
                "waitTime": 5,
                "chunkSize": 1024,
                "fileBase64": audio_base64,
            }

            if (
                self._token in self.blacklist_token
                or self._call_token in self.blacklist_call_token
            ):
                raise ValueError('token or call_token is forbidden to send request')
            await self._ws_asr.send(json.dumps(message))

            # 4. 接收返回数据
            try:
                flag = False
                while self._ws_asr.open:
                    if (
                        self._token in self.blacklist_token
                        or self._call_token in self.blacklist_call_token
                    ):
                        raise ValueError(
                            'token or call_token is forbidden to send request'
                        )
                    try:
                        if flag:
                            recv_data = await asyncio.wait_for(
                                self._ws_asr.recv(), timeout=4
                            )
                        else:
                            recv_data = await self._ws_asr.recv()
                    except asyncio.TimeoutError:
                        await on_completed(file_url)
                        logging.info('service completed with timeout')
                        break

                    if isinstance(recv_data, str):
                        recv_data = str(recv_data)
                        recv_data = json.loads(recv_data)

                        if recv_data.get('success', False):
                            await on_ready(file_url)
                            flag = True
                            continue

                        if recv_data.get('code', None) == 503:
                            self.blacklist_token.append(self._token)
                            self.blacklist_call_token.append(self._call_token)
                            raise ValueError('token or call_token is invalid')

                        if recv_data.get('end', False):
                            await on_completed(file_url)
                            break

                        await on_response(file_url, recv_data)

                    else:
                        raise Exception("Received data is not str")
            except ConnectionClosedError as e:
                logging.error('ConnectionClosedError')
                # raise e
            except Exception as e:
                raise e
            logging.info('service completed')

    @staticmethod
    async def _send_data(websocket, file_path):
        with open(file_path, 'rb') as f:
            # 去除wav头文件
            f.seek(44)
            while True:
                data = f.read(3200)
                if not data:
                    break
                await websocket.send(data)
                # print('send data')
                # print(datetime.datetime.now())
                # 100ms延迟
                await asyncio.sleep(0.6)

        await asyncio.sleep(10)
        await websocket.send('{"end": true}')
        # print(datetime.datetime.now())

        # print('------------------send end------------------')

    @staticmethod
    async def _receive_data(
        websocket,
        request,
        on_ready,
        on_response,
        on_completed,
    ):
        # count = 0
        try:
            while True:
                resp = await websocket.recv()
                resp_json = json.loads(resp)

                if 'success' in resp_json and bool(resp_json['success']):
                    print('ready')
                    await on_ready()
                    continue

                if request.final_result is False:
                    await on_response(resp_json)
                    continue

                if (
                    'asr_results' in resp_json
                    and 'final_result' in resp_json['asr_results']
                    and bool(resp_json['asr_results']['final_result'])
                ):
                    await on_response(resp_json)
                    # print('------------------------------')
                    # print(count)
                    # count += 1
                    # print('recv resp:', resp_json)
                    # print('------------------------------')
        except websockets.exceptions.ConnectionClosedOK:
            # print('ConnectionClosedOK')
            await on_completed()

    async def asr_direct(
        self,
        request: ai_cloud_sdk_4pd_models.ASRRequest = None,
        on_ready: callable = None,
        on_response: callable = None,
        on_completed: callable = None,
    ):
        # print('-------------test asr-------------')

        file_path = request.audio_url

        hello_message = '{"parameter": {"lang": null,"enable_words": true}}'

        async with websockets.connect(
            'ws://172.26.1.45:31529/recognition',
            ping_timeout=60,
            ping_interval=60,
            close_timeout=60,
        ) as websocket:
            await websocket.send(hello_message)
            # print('send hello message')
            resp = await websocket.recv()
            # print('recv resp:', resp)

            # 创建并发任务：一个发送数据，一个接收数据
            send_task = asyncio.create_task(self._send_data(websocket, file_path))
            receive_task = asyncio.create_task(
                self._receive_data(
                    websocket, request, on_ready, on_response, on_completed
                )
            )

            # 等待发送任务完成
            await send_task
            # 等待接收任务完成
            await receive_task

    async def asr_direct_vi(
        self,
        request: ai_cloud_sdk_4pd_models.ASRRequest = None,
        on_ready: callable = None,
        on_response: callable = None,
        on_completed: callable = None,
    ):
        # print('-------------test asr-------------')

        file_path = request.audio_url

        hello_message = '{"parameter": {"lang": null,"enable_words": true}}'

        async with websockets.connect(
            'ws://172.26.1.45:23238/recognition',
            ping_timeout=60,
            ping_interval=60,
            close_timeout=60,
        ) as websocket:
            await websocket.send(hello_message)
            # print('send hello message')
            resp = await websocket.recv()
            # print('recv resp:', resp)

            # 创建并发任务：一个发送数据，一个接收数据
            send_task = asyncio.create_task(self._send_data(websocket, file_path))
            receive_task = asyncio.create_task(
                self._receive_data(
                    websocket, request, on_ready, on_response, on_completed
                )
            )

            # 等待发送任务完成
            await send_task
            # 等待接收任务完成
            await receive_task
