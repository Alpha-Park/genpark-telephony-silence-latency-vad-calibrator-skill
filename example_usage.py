from client import TelephonySilenceLatencyVadCalibratorClient

def main():
    client = TelephonySilenceLatencyVadCalibratorClient()
    res = client.calibrate_endpointing_threshold(-38.0, 140, 50)
    print('VAD Calibrator: ' + res['calibration_id'])
    print('Silence Threshold: ' + str(res['optimal_silence_threshold_ms']) + 'ms | Total Latency: ' + str(res['end_of_speech_latency_ms']) + 'ms')
    print('Profile URL: ' + res['calibration_profile_url'])

if __name__ == '__main__':
    main()
