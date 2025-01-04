
import datetime
import time
import quote_module.quote_module as qm
from collections import defaultdict

dict_serial_number = defaultdict(int)


def callback_pcap_read(quote: qm.QuoteS):
    pass
    print(f'{quote.code_str} {quote.timestamp_str} {quote.close_price} {quote.bool_close} {quote.close_volume} '
          f'{quote.volume_acc} {quote.ask_price} {quote.ask_volume} {quote.bid_price} {quote.bid_volume} '
          f'{quote.bool_continue} {quote.bool_bid_price} {quote.bool_ask_price} {quote.bool_odd} '
          f'{quote.number_best_ask} {quote.number_best_bid} {quote.tick_type} {quote.bool_simtrade} '
          f'{quote.double_now_seconds} {quote.message_type} {quote.serial_number}')

    last_serial_number = dict_serial_number[quote.message_type]
    if quote.serial_number != last_serial_number + 1:
        print(f'Error: {quote.message_type} {quote.serial_number} {last_serial_number}')
    dict_serial_number[quote.message_type] = quote.serial_number


if False:
    qm.INTERFACE_IP_TSE = '10.175.2.17' 
    qm.INTERFACE_IP_OTC = '10.175.1.17' 
    qm.INTERFACE_IP_FUT = '10.71.17.74'
    qm.set_mc_live_pcap_callback(callback_pcap_read)
    qm.start_mc_live_pcap_read()


if True:
    qm.set_offline_pcap_callback(callback_pcap_read)
    qm.start_offline_pcap_read('/home/william/tcpdump/TSEOTC-2025-01-02.pcap')


while True:
    ret = qm.check_offline_pcap_read_ended()
    if ret != 0:
        break
    print(f'{datetime.datetime.now()} {ret}')
    time.sleep(1)
