# Stream Avro schema to Bigquery

Put your gcp credentials inside <b>service_account</b> folder
### How to use:

1. Feed GOOGLE_APPLICATION_CREDENTIALS with path to your service account json file
2. Build the container 
   ```bash
   docker compose up
   ```
3. Edit whatever table or dataset names as you want on consumer.py file
4. Open two terminal and run each terminal like the following:
   ```bash
   python producer.py
   ```
   ```bash
   python consumer.py
   ```

Now you can check if the data streamed like this:
![Streamed Data](https://github.com/Galihbagusp/kafka-python-code/blob/master/bitcoin_bigquery/imgs/preview_table.png?raw=true)

![Streamed Data](https://github.com/Galihbagusp/kafka-python-code/blob/master/bitcoin_bigquery/imgs/bit_coin_dataset.png?raw=true)



 
   
