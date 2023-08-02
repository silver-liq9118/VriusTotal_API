import requests

def get_ip_analysis(api_key, ip):
    url = f'https://www.virustotal.com/api/v3/ip_addresses/{ip}'
    headers = {
    'x-apikey': api_key,
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200: 
        data = response.json()
        last_analysis_results = data['data']['attributes']['last_analysis_results']
        malicious_results = [engine_result['result'] for engine_result in last_analysis_results.values() if engine_result['category'] == 'malicious']
        print(ip,': ',malicious_results)
    else:
        print(f"Error {response.status_code}: {response.text}")

if __name__ == '__main__':
    api_key = '' # 본인의 VirusTotal API 키
    start_ip_range = 0  # 시작 IP 
    end_ip_range = 5   # 종료 IP 

    for i in range(start_ip_range, end_ip_range):
        ip = #dataset
        get_ip_analysis(api_key, ip)
