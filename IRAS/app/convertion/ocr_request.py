from .ecloud import CMSSEcloudOcrClient
#OCR service module
accesskey = '57982d9c5fe241809f883b2c6e5fd035'
secretkey = 'a9054e8f41c849e8aacf366c30507659'
url = 'https://api-wuxi-1.cmecloud.cn:8443'

def get_response(image_path):
    print('using ecloud ocr service...')
    requesturl = '/api/ocr/v1/general'
    options = {}
    options['TemplateId'] = '76542407608369152'
    try:
        ocr_client = CMSSEcloudOcrClient(accesskey, secretkey, url)
        response = ocr_client.request_ocr_service_file(requestpath=requesturl, imagepath= image_path, options=options)
            # get response from ocr_client
    except ValueError as e:
        print(e)
    return response

if __name__ == '__main__':
    image_path = ""
    get_response(image_path)