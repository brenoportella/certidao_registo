from src.log_config import logger
from src.read_codes import read_codes
from src.create_report import generate_report
from src.threads_exec import get_results

def main():
    logger.info('=== START EXECUTION ===')

    ano_destino = input('Write the selected year to be checked (e.g.: 2023): ')
    try:
        # 1. Ler códigos
        codigos = read_codes()
        logger.info(f'Total number of codes: {len(codigos)}')

        # 2. Processar em paralelo
        resultados = get_results(codigos)

        # 3. Gerar relatório
        generate_report(resultados, ano_destino)

    except Exception as e:
        logger.critical(f'Erro fatal: {str(e)}')
    finally:
        logger.info('=== END EXECUTION ===')

if __name__ == '__main__':
    main()
