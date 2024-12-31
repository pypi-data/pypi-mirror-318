import requests
import urllib.request
import base64
import random
import time
from selenium import webdriver
def oca_solve_captcha(user_api_key, action_type, number_captcha_attempts, wait_captcha_seconds):
    if not number_captcha_attempts or number_captcha_attempts <= 0:
        number_captcha_attempts = 1
    if not wait_captcha_seconds or wait_captcha_seconds <= 0:
        wait_captcha_seconds = 0
    action_type = action_type.lower()
    if action_type == "tiktokcircle" or action_type == "tiktokpuzzle" or action_type == "tiktok3d" or action_type == "tiktokicon":
        try:
            start_time = time.time()
            while time.time() - start_time < wait_captcha_seconds:
                is_exist_capctha_whirl = driver.execute_script("""var elements = document.evaluate('//div[contains(@class,"captcha_verify_container")]/div/img[1][contains(@style,"transform: translate(-50%, -50%) rotate")] | //div[contains(@class, "cap") and count(img) = 2 and contains(img/@style, "circle")]', document, null, XPathResult.UNORDERED_NODE_SNAPSHOT_TYPE, null); return elements.snapshotLength > 0;""")        
                is_exist_capctha_slide = driver.execute_script("""var elements = document.evaluate('//div[contains(@class,"captcha_verify_img")]/img[contains(@class,"captcha_verify_img_slide")]/following::div/following::div//div[contains(@class,"captcha-drag-icon")]', document, null, XPathResult.UNORDERED_NODE_SNAPSHOT_TYPE, null); return elements.snapshotLength > 0;""")             
                is_exist_3d_capctha = driver.execute_script("""var elements = document.evaluate('//div[contains(@class,"captcha_verify_img")]/img | //div[contains(@class,"cap")]//img/following-sibling::button/parent::div/parent::div/parent::div/div//img[contains(@src,"/3d_") and //div[contains(@class,"cap")]//img/following-sibling::button]', document, null, XPathResult.UNORDERED_NODE_SNAPSHOT_TYPE, null); return elements.snapshotLength > 0;""")
                is_exist_icon_capctha = driver.execute_script("""var elements = document.evaluate('//div[contains(@class,"cap")]//img/following-sibling::button/parent::div/parent::div/parent::div/div//img[contains(@src,"/icon_") and //div[contains(@class,"cap")]//img/following-sibling::button]', document, null, XPathResult.UNORDERED_NODE_SNAPSHOT_TYPE, null); return elements.snapshotLength > 0;""")
                if is_exist_capctha_whirl or is_exist_capctha_slide or is_exist_3d_capctha or is_exist_icon_capctha:
                    break
                time.sleep(1)
            for i in range(0, number_captcha_attempts):
                is_exist_capctha_whirl = driver.execute_script("""var elements = document.evaluate('//div[contains(@class,"captcha_verify_container")]/div/img[1][contains(@style,"transform: translate(-50%, -50%) rotate")] | //div[contains(@class, "cap") and count(img) = 2 and contains(img/@style, "circle")]', document, null, XPathResult.UNORDERED_NODE_SNAPSHOT_TYPE, null); return elements.snapshotLength > 0;""")        
                is_exist_capctha_slide = driver.execute_script("""var elements = document.evaluate('//div[contains(@class,"captcha_verify_img")]/img[contains(@class,"captcha_verify_img_slide")]/following::div/following::div//div[contains(@class,"captcha-drag-icon")]', document, null, XPathResult.UNORDERED_NODE_SNAPSHOT_TYPE, null); return elements.snapshotLength > 0;""")             
                is_exist_3d_capctha = driver.execute_script("""var elements = document.evaluate('//div[contains(@class,"captcha_verify_img")]/img | //div[contains(@class,"cap")]//img/following-sibling::button/parent::div/parent::div/parent::div/div//img[contains(@src,"/3d_") and //div[contains(@class,"cap")]//img/following-sibling::button]', document, null, XPathResult.UNORDERED_NODE_SNAPSHOT_TYPE, null); return elements.snapshotLength > 0;""")
                is_exist_icon_capctha = driver.execute_script("""var elements = document.evaluate('//div[contains(@class,"cap")]//img/following-sibling::button/parent::div/parent::div/parent::div/div//img[contains(@src,"/icon_") and //div[contains(@class,"cap")]//img/following-sibling::button]', document, null, XPathResult.UNORDERED_NODE_SNAPSHOT_TYPE, null); return elements.snapshotLength > 0;""")
                if not (is_exist_capctha_whirl or is_exist_capctha_slide or is_exist_3d_capctha or is_exist_icon_capctha): 
                    break
                else:
                    get_refresh_buttton = driver.execute_script("""var elements = document.evaluate('//a[contains(@class,"refresh")]/span[contains(@class,"refresh")][text()] | //button[contains(@class,"cap-items")][1]', document, null, XPathResult.UNORDERED_NODE_SNAPSHOT_TYPE, null); return elements.snapshotLength > 0;""")
                    if get_refresh_buttton:
                        update_captcha_img = driver.execute_script("""var element = document.evaluate('/a[contains(@class,"refresh")]/span[contains(@class,"refresh")][text()] | //button[contains(@class,"cap-items")][1]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue; return element;""")
                    else:
                        update_captcha_img = driver.execute_script("""var element = document.evaluate('//div[contains(@class,"captcha_verify_action")]//button[1]//div[contains(@class,"Button-label")][text()]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue; return element;""")
                    
                    if is_exist_capctha_whirl:
                        get_full_img_url = driver.execute_script("""var elements = document.evaluate('//div[contains(@class,"captcha_verify_container")]/div/img[1][contains(@style,"transform: translate(-50%, -50%) rotate")] | //div[contains(@class, "cap") and count(img) = 2 and contains(img/@style, "circle")]/img[1]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null); var imgElement = elements.singleNodeValue; if (imgElement) {return imgElement.getAttribute("src");} return null;""")                        
                        open_full_img_url = urllib.request.urlopen(get_full_img_url)
                        full_img_url_html_bytes = open_full_img_url.read()
                        full_screenshot_img_url_base64 = base64.b64encode(full_img_url_html_bytes).decode('utf-8')
                        full_img = full_screenshot_img_url_base64
                        get_slider_square = driver.execute_script("""var element = document.evaluate('//div[contains(@class,"slidebar")] | //div[contains(@class, "cap")]/div[contains(@draggable, "true")]/parent::div', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue; if (element) {var width = window.getComputedStyle(element).getPropertyValue("width"); var height = window.getComputedStyle(element).getPropertyValue("height"); return {width: Math.round(parseFloat(width)), height: Math.round(parseFloat(height))};}return null;""")                      
                        img_width = get_slider_square['width']
                        img_height = get_slider_square['height']
                        small_img_url = driver.execute_script("""var elements = document.evaluate('//div[contains(@class,"captcha_verify_container")]/div/img[1][contains(@style,"transform: translate(-50%, -50%) rotate")] | //div[contains(@class, "cap") and count(img) = 2 and contains(img/@style, "circle")]/img[2]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null); var imgElement = elements.singleNodeValue; if (imgElement) {return imgElement.getAttribute("src");} return null;""")                        
                        open_small_img_url = urllib.request.urlopen(small_img_url)
                        small_img_url_html_bytes = open_small_img_url.read()
                        small_screenshot_img_url_base64 = base64.b64encode(small_img_url_html_bytes).decode('utf-8')
                        small_img = small_screenshot_img_url_base64
                        captcha_action_type = "tiktokCircle"
                        multipart_form_data = {
                            'FULL_IMG_CAPTCHA': (None, full_img),
                            'SMALL_IMG_CAPTCHA': (None, small_img),
                            'FULL_IMG_WIDTH': (None, img_width),
                            'FULL_IMG_HEIGHT': (None, img_height),
                            'ACTION': (None, captcha_action_type),
                            'USER_KEY': (None, user_api_key)
                        }
                        request_solve_captcha = requests.post('https://captcha.ocasoft.com/api/res.php', files=multipart_form_data)
                        response_solve_captcha_content = request_solve_captcha.content
                        if isinstance(response_solve_captcha_content, bytes):
                            response_solve_captcha_content = response_solve_captcha_content.decode('utf-8')
                        if response_solve_captcha_content == "ERROR_USER_KEY":
                            raise Exception("Invalid API key / Make sure you using correct API key")
                        elif response_solve_captcha_content == "INVALID_ACTION":
                            raise Exception("Invalid action type / Supports: tiktokCircle, tiktokPuzzle, tiktok3D, tiktokIcon")
                        elif response_solve_captcha_content == "ZERO_BALANCE":
                            raise Exception("Balance is zero / Top up your balance")
                        if response_solve_captcha_content.strip().startswith('{') and response_solve_captcha_content.strip().endswith('}'):
                            response_solve_captcha = request_solve_captcha.json()
                            response_cordinate_x = int(response_solve_captcha["cordinate_x"])
                            response_cordinate_y = int(response_solve_captcha["cordinate_y"])
                            driver.execute_script("""var element = document.evaluate('//div[contains(@class,"secsdk-captcha-drag-icon")]//*[name()="svg"] | //div[contains(@class, "cap")]/div[contains(@draggable, "true")]/button//*[name()="svg"]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue; if (element) {var rect = element.getBoundingClientRect(); var startX = rect.left + rect.width / 2; var startY = rect.top + rect.height / 2; var totalOffsetX = arguments[0]; var duration = 1000; var steps = 150; var stepDelay = duration / steps; var stepX = totalOffsetX / steps; var currentX = startX; var currentY = startY; var dragStartEvent = new DragEvent('dragstart', {bubbles: true, cancelable: true, clientX: startX, clientY: startY}); element.dispatchEvent(dragStartEvent); var interval = setInterval(() => {currentX += stepX; var moveEvent = new DragEvent('drag', {bubbles: true, cancelable: true, clientX: currentX, clientY: currentY}); element.dispatchEvent(moveEvent); if (currentX >= startX + totalOffsetX) {clearInterval(interval); var dropEvent = new DragEvent('drop', {bubbles: true, cancelable: true, clientX: currentX, clientY: currentY}); element.dispatchEvent(dropEvent); var dragEndEvent = new DragEvent('dragend', {bubbles: true, cancelable: true, clientX: currentX, clientY: currentY}); element.dispatchEvent(dragEndEvent);}}, stepDelay);}""", response_cordinate_x)
                            time.sleep(random.uniform(8, 10))
                        else:
                            driver.execute_script("arguments[0].click();", update_captcha_img)
                            time.sleep(random.uniform(8, 10))

                    if is_exist_capctha_slide:
                        get_full_img_url = driver.execute_script("""var elements = document.evaluate('//div[contains(@class,"captcha_verify_img")]/img[contains(@id,"captcha-verify-image")] | //div[contains(@class, "cap") and count(img) = 1]/img/following-sibling::div/img/parent::div/parent::div', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null); var imgElement = elements.singleNodeValue; if (imgElement) {return imgElement.getAttribute("src");} return null;""")                        
                        open_full_img_url = urllib.request.urlopen(get_full_img_url)
                        full_img_url_html_bytes = open_full_img_url.read()
                        full_screenshot_img_url_base64 = base64.b64encode(full_img_url_html_bytes).decode('utf-8')
                        full_img = full_screenshot_img_url_base64
                        get_slider_square = driver.execute_script("""var element = document.evaluate('//div[contains(@class,"slidebar")] | //div[contains(@class, "cap")]/div[contains(@draggable, "true")]/parent::div', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue; if (element) {var width = window.getComputedStyle(element).getPropertyValue("width"); var height = window.getComputedStyle(element).getPropertyValue("height"); return {width: Math.round(parseFloat(width)), height: Math.round(parseFloat(height))};}return null;""")                      
                        img_width = get_slider_square['width']
                        img_height = get_slider_square['height']  
                        small_img_url = driver.execute_script("""var elements = document.evaluate('//div[contains(@class,"captcha_verify_img")]/img[contains(@class,"captcha_verify_img_slide")] | //div[contains(@class, "cap") and count(img) = 1]/img/following-sibling::div/img/parent::div', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null); var imgElement = elements.singleNodeValue; if (imgElement) {return imgElement.getAttribute("src");} return null;""")
                        open_small_img_url = urllib.request.urlopen(small_img_url)
                        small_img_url_html_bytes = open_small_img_url.read()
                        small_screenshot_img_url_base64 = base64.b64encode(small_img_url_html_bytes).decode('utf-8')
                        small_img = small_screenshot_img_url_base64
                        captcha_action_type = "tiktokPuzzle"
                        multipart_form_data = {
                            'FULL_IMG_CAPTCHA': (None, full_img),
                            'SMALL_IMG_CAPTCHA': (None, small_img),
                            'FULL_IMG_WIDTH': (None, img_width),
                            'FULL_IMG_HEIGHT': (None, img_height),
                            'ACTION': (None, captcha_action_type),
                            'USER_KEY': (None, user_api_key)
                        }
                        request_solve_captcha = requests.post('https://captcha.ocasoft.com/api/res.php', files=multipart_form_data)
                        response_solve_captcha_content = request_solve_captcha.content
                        if isinstance(response_solve_captcha_content, bytes):
                            response_solve_captcha_content = response_solve_captcha_content.decode('utf-8')
                        if response_solve_captcha_content == "ERROR_USER_KEY":
                            raise Exception("Invalid API key / Make sure you using correct API key")
                        elif response_solve_captcha_content == "INVALID_ACTION":
                            raise Exception("Invalid action type / Supports: tiktokCircle, tiktokPuzzle, tiktok3D, tiktokIcon")
                        elif response_solve_captcha_content == "ZERO_BALANCE":
                            raise Exception("Balance is zero / Top up your balance")
                        if response_solve_captcha_content.strip().startswith('{') and response_solve_captcha_content.strip().endswith('}'):
                            response_cordinate_x = int(response_solve_captcha["cordinate_x"])
                            response_cordinate_y = int(response_solve_captcha["cordinate_y"])
                            time.sleep(random.uniform(0.1, 1))
                            driver.execute_script("""var element = document.evaluate('//div[contains(@class,"secsdk-captcha-drag-icon")]//*[name()="svg"] | //div[contains(@class, "cap")]/div[contains(@draggable, "true")]/button//*[name()="svg"]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue; if (element) {var rect = element.getBoundingClientRect(); var startX = rect.left + rect.width / 2; var startY = rect.top + rect.height / 2; var totalOffsetX = arguments[0]; var duration = 1000; var steps = 150; var stepDelay = duration / steps; var stepX = totalOffsetX / steps; var currentX = startX; var currentY = startY; var dragStartEvent = new DragEvent('dragstart', {bubbles: true, cancelable: true, clientX: startX, clientY: startY}); element.dispatchEvent(dragStartEvent); var interval = setInterval(() => {currentX += stepX; var moveEvent = new DragEvent('drag', {bubbles: true, cancelable: true, clientX: currentX, clientY: currentY}); element.dispatchEvent(moveEvent); if (currentX >= startX + totalOffsetX) {clearInterval(interval); var dropEvent = new DragEvent('drop', {bubbles: true, cancelable: true, clientX: currentX, clientY: currentY}); element.dispatchEvent(dropEvent); var dragEndEvent = new DragEvent('dragend', {bubbles: true, cancelable: true, clientX: currentX, clientY: currentY}); element.dispatchEvent(dragEndEvent);}}, stepDelay);}""", response_cordinate_x)
                            time.sleep(random.uniform(8, 10))
                        else:
                            driver.execute_script("arguments[0].click();", update_captcha_img)
                            time.sleep(random.uniform(8, 10))

                    if is_exist_icon_capctha:
                        get_captcha_data = driver.execute_script("""var imgElement = document.evaluate('//div[contains(@class,"cap")]//img/following-sibling::button/parent::div/parent::div/parent::div/div//img[contains(@src,"/icon_")]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue; var questionElement = document.evaluate('//div[contains(@class,"cap")]//img/following-sibling::button/parent::div/parent::div/parent::div/div//span[text()]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue; if (imgElement && questionElement) {var imgWidth = imgElement.width; var imgHeight = imgElement.height; var imgCoordinates = imgElement.getBoundingClientRect(); return {imgWidth: imgWidth, imgHeight: imgHeight, imgX: imgCoordinates.left, imgY: imgCoordinates.top, question: questionElement.textContent};}""")
                        img_width = get_captcha_data['imgWidth']
                        img_height = get_captcha_data['imgHeight']
                        coordinate_full_img_url_x = get_captcha_data['imgX']
                        coordinate_full_img_url_y = get_captcha_data['imgY']
                        get_question = get_captcha_data['question']
                        get_full_img_url = driver.execute_script("""var elements = document.evaluate('//div[contains(@class,"cap")]//img/following-sibling::button/parent::div/parent::div/parent::div/div//img[contains(@src,"/icon_")]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null); var imgElement = elements.singleNodeValue; if (imgElement) {return imgElement.getAttribute("src");} return null;""")           
                        open_full_img_url = urllib.request.urlopen(get_full_img_url)
                        full_img_url_html_bytes = open_full_img_url.read()
                        full_screenshot_img_url_base64 = base64.b64encode(full_img_url_html_bytes).decode('utf-8')
                        full_img = full_screenshot_img_url_base64
                        captcha_action_type = "tiktokIcon"
                        multipart_form_data = {
                            'FULL_IMG_CAPTCHA': (None, full_img),
                            'CAPTCHA_QUESTION': (None, get_question),
                            'FULL_IMG_WIDTH': (None, img_width),
                            'FULL_IMG_HEIGHT': (None, img_height),
                            'ACTION': (None, captcha_action_type),
                            'USER_KEY': (None, user_api_key)
                        }   
                        request_solve_captcha = requests.post('https://captcha.ocasoft.com/api/res.php', files=multipart_form_data)
                        response_solve_captcha_content = request_solve_captcha.content
                        if isinstance(response_solve_captcha_content, bytes):
                            response_solve_captcha_content = response_solve_captcha_content.decode('utf-8')
                        if response_solve_captcha_content == "ERROR_USER_KEY":
                            raise Exception("Invalid API key / Make sure you using correct API key")
                        elif response_solve_captcha_content == "INVALID_ACTION":
                            raise Exception("Invalid action type / Supports: tiktokCircle, tiktokPuzzle, tiktok3D, tiktokIcon")
                        elif response_solve_captcha_content == "ZERO_BALANCE":
                            raise Exception("Balance is zero / Top up your balance")
                        if response_solve_captcha_content.strip().startswith('{') and response_solve_captcha_content.strip().endswith('}'):
                            json_solve_captcha_data = request_solve_captcha.json()
                            coordinates = [(f"cordinate_x{i}", f"cordinate_y{i}") for i in range(1, len(json_solve_captcha_data) // 2 + 1)]
                            target_coordinates = []
                            for x_key, y_key in coordinates:
                                cordinate_x = int(json_solve_captcha_data[x_key])
                                cordinate_y = int(json_solve_captcha_data[y_key])
                                random_move_number = random.randint(1, 2)
                                random_click_coordinates = random.randint(0, 5)
                                if random_move_number == 1:
                                    target_cordinate_x = cordinate_x + coordinate_full_img_url_x - random_click_coordinates
                                    target_cordinate_y = cordinate_y + coordinate_full_img_url_y - random_click_coordinates
                                else:
                                    target_cordinate_x = cordinate_x + coordinate_full_img_url_x + random_click_coordinates
                                    target_cordinate_y = cordinate_y + coordinate_full_img_url_y + random_click_coordinates
                                target_coordinates.append((target_cordinate_x, target_cordinate_y))
                            time.sleep(random.uniform(0.1, 1))
                            for target_cordinate_x, target_cordinate_y in target_coordinates:
                                driver.execute_script("""var targetX1 = arguments[0]; var targetY1 = arguments[1]; var mouseEvent1 = new MouseEvent('mousemove', { clientX: targetX1, clientY: targetY1, bubbles: true, cancelable: true }); document.elementFromPoint(targetX1, targetY1).dispatchEvent(mouseEvent1); var mouseClick1 = new MouseEvent('click', { clientX: targetX1, clientY: targetY1, bubbles: true, cancelable: true }); document.elementFromPoint(targetX1, targetY1).dispatchEvent(mouseClick1); """, target_cordinate_x, target_cordinate_y)
                                time.sleep(random.uniform(0.05, 1))                        
                            driver.execute_script("""var submitButton = document.evaluate('//div[contains(@class,"verify-captcha-submit-button")] | //div[contains(@class,"cap")]//img/following-sibling::button', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue; if (submitButton) {submitButton.click();}""")
                            time.sleep(random.uniform(8, 10))
                        else:
                            driver.execute_script("arguments[0].click();", update_captcha_img)
                            time.sleep(random.uniform(8, 10))
                                                                       
                    if is_exist_3d_capctha:
                        get_captcha_data = driver.execute_script("""var imgElement = document.evaluate('//div[contains(@class,"captcha_verify_img")]/img | //div[contains(@class,"cap")]//img/following-sibling::button/parent::div/parent::div/parent::div/div//img[contains(@src,"/3d_")]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue; if (imgElement) {var imgRect = imgElement.getBoundingClientRect(); return {width: imgElement.width, height: imgElement.height, x: imgRect.left + window.scrollX, y: imgRect.top + window.scrollY};} else {return null;}""")
                        img_width = round(get_captcha_data['width'])
                        img_height = round(get_captcha_data['height'])
                        coordinate_full_img_url_x = round(get_captcha_data['x'])
                        coordinate_full_img_url_y = round(get_captcha_data['y'])
                        get_full_img_url = driver.execute_script("""var elements = document.evaluate('//div[contains(@class,"captcha_verify_img")]/img | //div[contains(@class,"cap")]//img/following-sibling::button/parent::div/parent::div/parent::div/div//img[contains(@src,"/3d_")]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null); var imgElement = elements.singleNodeValue; if (imgElement) {return imgElement.getAttribute("src");} return null;""")                        
                        open_full_img_url = urllib.request.urlopen(get_full_img_url)
                        full_img_url_html_bytes = open_full_img_url.read()
                        full_screenshot_img_url_base64 = base64.b64encode(full_img_url_html_bytes).decode('utf-8')
                        full_img = full_screenshot_img_url_base64
                        captcha_action_type = "tiktok3D"
                        multipart_form_data = {
                            'FULL_IMG_CAPTCHA': (None, full_img),
                            'FULL_IMG_WIDTH': (None, img_width),
                            'FULL_IMG_HEIGHT': (None, img_height),
                            'ACTION': (None, captcha_action_type),
                            'USER_KEY': (None, user_api_key)
                        }   
                        request_solve_captcha = requests.post('https://captcha.ocasoft.com/api/res.php', files=multipart_form_data)
                        response_solve_captcha_content = request_solve_captcha.content
                        if isinstance(response_solve_captcha_content, bytes):
                            response_solve_captcha_content = response_solve_captcha_content.decode('utf-8')
                        if response_solve_captcha_content == "ERROR_USER_KEY":
                            raise Exception("Invalid API key / Make sure you using correct API key")
                        elif response_solve_captcha_content == "INVALID_ACTION":
                            raise Exception("Invalid action type / Supports: tiktokCircle, tiktokPuzzle, tiktok3D, tiktokIcon")
                        elif response_solve_captcha_content == "ZERO_BALANCE":
                            raise Exception("Balance is zero / Top up your balance")
                        if response_solve_captcha_content.strip().startswith('{') and response_solve_captcha_content.strip().endswith('}'):
                            json_solve_captcha_data = request_solve_captcha.json()
                            print(json_solve_captcha_data)
                            cordinate_x1 = int(json_solve_captcha_data["cordinate_x1"])
                            cordinate_y1 = int(json_solve_captcha_data["cordinate_y1"])
                            cordinate_x2 = int(json_solve_captcha_data["cordinate_x2"])
                            cordinate_y2 = int(json_solve_captcha_data["cordinate_y2"])
                            random_move_number = random.randint(1, 2)
                            random_click_coordinates = random.randint(0, 5)
                            if random_move_number == 1:
                                target_cordinate_x1 = int(cordinate_x1) + int(coordinate_full_img_url_x) - int(random_click_coordinates)
                                target_cordinate_y1 = int(cordinate_y1) + int(coordinate_full_img_url_y) - int(random_click_coordinates)
                                target_cordinate_x2 = int(cordinate_x2) + int(coordinate_full_img_url_x) - int(random_click_coordinates)
                                target_cordinate_y2 = int(cordinate_y2) + int(coordinate_full_img_url_y) - int(random_click_coordinates)
                            else:
                                target_cordinate_x1 = int(cordinate_x1) + int(coordinate_full_img_url_x) + int(random_click_coordinates)
                                target_cordinate_y1 = int(cordinate_y1) + int(coordinate_full_img_url_y) + int(random_click_coordinates)
                                target_cordinate_x2 = int(cordinate_x2) + int(coordinate_full_img_url_x) + int(random_click_coordinates)
                                target_cordinate_y2 = int(cordinate_y2) + int(coordinate_full_img_url_y) + int(random_click_coordinates)
                            time.sleep(random.uniform(0.1, 1))
                            driver.execute_script("""var targetX1 = arguments[0]; var targetY1 = arguments[1]; var mouseEvent1 = new MouseEvent('mousemove', { clientX: targetX1, clientY: targetY1, bubbles: true, cancelable: true }); document.elementFromPoint(targetX1, targetY1).dispatchEvent(mouseEvent1); var mouseClick1 = new MouseEvent('click', { clientX: targetX1, clientY: targetY1, bubbles: true, cancelable: true }); document.elementFromPoint(targetX1, targetY1).dispatchEvent(mouseClick1); """, target_cordinate_x1, target_cordinate_y1)
                            time.sleep(random.uniform(0.05, 1))
                            driver.execute_script("""var targetX2 = arguments[0]; var targetY2 = arguments[1]; var mouseEvent2 = new MouseEvent('mousemove', { clientX: targetX2, clientY: targetY2, bubbles: true, cancelable: true }); document.elementFromPoint(targetX2, targetY2).dispatchEvent(mouseEvent2); var mouseClick2 = new MouseEvent('click', { clientX: targetX2, clientY: targetY2, bubbles: true, cancelable: true }); document.elementFromPoint(targetX2, targetY2).dispatchEvent(mouseClick2); """, target_cordinate_x2, target_cordinate_y2)
                            time.sleep(random.uniform(0.05, 1))    
                            driver.execute_script("""var submitButton = document.evaluate('//div[contains(@class,"verify-captcha-submit-button")] | //div[contains(@class,"cap")]//img/following-sibling::button', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue; if (submitButton) {submitButton.click();}""")
                            time.sleep(random.uniform(8, 10))
                        else:
                            driver.execute_script("arguments[0].click();", update_captcha_img)
                            time.sleep(random.uniform(8, 10))
                            
        except Exception as e:
            print(f"Error: {e}")
    elif action_type == "datadomeaudio" or action_type == "datadomeimage":
        try:
            print("datadomeaudio")
        except Exception as e:
            print(f"Error: {e}")
    elif action_type == "geetesticon":
        try:
            print("geetesticon")
        except Exception as e:
            print(f"Error: {e}")
    else:
        ("Invalid action type / Supports: tiktokCircle, tiktokPuzzle, tiktok3D, tiktokIcon, dataDomeAudio, dataDomeImage, geetestIcon")