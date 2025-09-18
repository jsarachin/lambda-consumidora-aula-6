import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logger.info("Lambda iniciada com sucesso!")

    for record in event['Records']:
        body = record['body']
        logger.info(f"Leitura da fila:{body}")

    return {
        'statusCode': 200,
        'body': json.dumps('Mensagens processadas com sucesso!')
    }