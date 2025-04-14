from src.code_process import process_code
from src.driver import quit_driver, setup_driver
from src.log_config import logger

def get_results(codes):
    results = []

    companies = len(codes)

    for i, code in enumerate (codes, 1):
        driver = setup_driver()
        logger.info(f'Processando empresa {i} de {companies} - code {code}')
        try:
            driver.get(f"https://registo.justica.gov.pt/Empresas/Consultar-Certidao-Permanente/Iniciar?codcertidao={code}")
            result = process_code(driver=driver, code=code)
            results.append(result)

            driver.delete_all_cookies()
            driver.get("about:blank")
        except Exception as e:
            logger.error(f"Erro no código {code}: {str(e)}")
            results.append({
                'Code': code,
                'Status': 'ERRO',
                'NIF': '',
                'Company': '',
                'Error': str(e),
            })
        finally:
            quit_driver(driver)

    return results