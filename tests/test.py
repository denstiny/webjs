import os
import sys
from webjs import webjs
from webjs.JsType import *

class MWEBJS(webjs.JSDemo):
    async def appmain(self):
        aweme_id = "7356672812599299343"
        cursor = 0
        count = 20
        msToken = "vZHoRDPsiJAL5cowL1pLFbhppUtOUixaLQGLB9b-3J6uWJtIwwqZisXsqzBUq21QT3qatSR5xEzUqrbUf89OJgU-CyxqyAWr8fAs-W_t5vnM7UZbsoJrUw%3D%3D"

        device = f'device_platform=webapp&aid=6383&channel=channel_pc_web&aweme_id={aweme_id}&cursor={cursor}&count={count}&item_type=0&insert_ids=&whale_cut_token=&cut_version=1&rcFT=&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1920&screen_height=1200&browser_language=zh&browser_platform=Win32&browser_name=Edge&browser_version=120.0.2276.80&browser_online=true&engine_name=Blink&engine_version=122.0.6285.217&os_name=Windows&os_version=10&cpu_core_num=12&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=100&webid=7356175988425049638&msToken={msToken}'

        res = await self.call(f'completeXB({js_s(device)});')
        print(res)



if __name__ == "__main__":
    #loop = asyncio.get_event_loop()
    #loop.run_until_complete(DouyinTask())
    m = MWEBJS()
    PROJECT_ROOT = os.path.dirname(sys.argv[0])
    print(PROJECT_ROOT)
    m.loadHtml(f"{PROJECT_ROOT}/core/app.html")
    m.startApp()
