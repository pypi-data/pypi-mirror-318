import ai_cloud_sdk_4pd.client as ai_cloud_sdk_4pd_client
import ai_cloud_sdk_4pd.models as ai_cloud_sdk_4pd_models

count = 0


async def on_ready(file_url):
    print(file_url + ':ready')


async def on_response(file_url, response):
    global count
    print('-------------------------------------')
    print(count)
    count += 1
    print(file_url + ':' + str(response))


async def on_completed(file_url):
    print(file_url + ':completed')


async def test_asr():
    print('-------------test asr-------------')
    token = 'eyJhbGciOiJIUzI1NiJ9.eyJ0ZW5hbnRfaWQiOjEsInRva2VuX2NyZWF0ZWRfYXQiOjE3MzI3NjUxMTMwNjYsImlhdCI6MTczMjc2NTExM30.tboPQVyJoKuPAbZVIOPJxI9wbr5TD5Mtck-8P59Fs2I'
    call_token = 'eyJhbGciOiJIUzI1NiJ9.eyJ0ZW5hbnRfaWQiOjEsInVzZXJfaWQiOjYsInRva2VuX2NyZWF0ZWRfYXQiOjE3MzMxOTY5Mzg0NTUsImlhdCI6MTczMzE5NjkzOH0.xPt2491jDWZQYCS3TpTSko3ln6xTApqg12m_T-P4FDk'
    region = 'China'
    config = ai_cloud_sdk_4pd_models.Config(
        token=token,
        call_token=call_token,
        region=region,
    )
    client = ai_cloud_sdk_4pd_client.Client(config=config)
    request = ai_cloud_sdk_4pd_models.ASRRequest(
        batch_directory='/Users/4paradigm/Desktop',
        language='ja',
    )

    await client.asr_batch(
        request=request,
        on_ready=on_ready,
        on_response=on_response,
        on_completed=on_completed,
    )


if __name__ == '__main__':
    import asyncio

    asyncio.get_event_loop().run_until_complete(test_asr())
