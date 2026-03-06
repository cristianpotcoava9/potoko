from seleniumbase import SB
import random
import base64
import requests
proxy_str = False
urlt = f"https://www.twitch.tv/brutalles"

while True:
    with SB(uc=True, locale="en", ad_block=True, chromium_arg='--disable-webgl', proxy=proxy_str) as gasssssssvx:
        rnd = random.randint(450, 800)

        gasssssssvx.activate_cdp_mode(urlt)
        gasssssssvx.sleep(2)

        # Accept cookies if present
        if gasssssssvx.is_element_present('button:contains("Accept")'):
            gasssssssvx.cdp.click('button:contains("Accept")', timeout=4)

        gasssssssvx.sleep(2)
        gasssssssvx.sleep(12)

        # Start watching if needed
        if gasssssssvx.is_element_present('button:contains("Start Watching")'):
            gasssssssvx.cdp.click('button:contains("Start Watching")', timeout=4)
            gasssssssvx.sleep(10)

        # Accept again if it pops up
        if gasssssssvx.is_element_present('button:contains("Accept")'):
            gasssssssvx.cdp.click('button:contains("Accept")', timeout=4)

        # Check if stream is live
        if gasssssssvx.is_element_present("#live-channel-stream-information"):

            # Accept if needed
            if gasssssssvx.is_element_present('button:contains("Accept")'):
                gasssssssvx.cdp.click('button:contains("Accept")', timeout=4)

            # Open second driver
            gasssssssvx2 = gasssssssvx.get_new_driver(undetectable=True)
            gasssssssvx2.activate_cdp_mode(urlt)
            gasssssssvx2.sleep(10)

            if gasssssssvx2.is_element_present('button:contains("Start Watching")'):
                gasssssssvx2.cdp.click('button:contains("Start Watching")', timeout=4)
                gasssssssvx2.sleep(10)

            if gasssssssvx2.is_element_present('button:contains("Accept")'):
                gasssssssvx2.cdp.click('button:contains("Accept")', timeout=4)

            gasssssssvx.sleep(rnd)

        else:
            break
