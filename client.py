class TelephonySilenceLatencyVadCalibratorClient:
    def calibrate_endpointing_threshold(self, background_noise_db=-42.0, speaker_cadence_wpm=135, network_rtt_ms=45):
        threshold_ms = 450 if speaker_cadence_wpm < 120 else 320
        return {
            'calibration_id': 'vad_cal_8812',
            'optimal_silence_threshold_ms': threshold_ms,
            'adaptive_speech_end_detected': True,
            'false_interruption_probability_pct': 1.8,
            'end_of_speech_latency_ms': threshold_ms + network_rtt_ms,
            'calibration_profile_url': 'https://elevenlabs.vad.genpark.ai/profiles/8812.json'
        }
