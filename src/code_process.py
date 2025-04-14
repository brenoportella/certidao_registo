import re
import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src.defines import MAX_RETRIES, TIME_WAIT
from src.log_config import logger


def process_code(driver, code):
    attempts = 0
    last_exception = None

    while attempts < MAX_RETRIES:
        try:
            logger.info(f'Try number {attempts + 1} for the code: {code}')

            try:
                driver.get(
                    f'https://registo.justica.gov.pt/Empresas/Consultar-Certidao-Permanente/Iniciar?codcertidao={code}'
                )

                try:
                    wait = WebDriverWait(driver, TIME_WAIT)
                    
                    nif = wait.until(
                        EC.visibility_of_element_located(
                            (
                                By.XPATH,
                                "//td[contains(text(), 'NIF/NIPC:')]/following-sibling::td",
                            )
                        )
                    ).text

                    company = wait.until(
                        EC.visibility_of_element_located(
                            (
                                By.XPATH,
                                "//td[contains(text(), 'Firma:')]/following-sibling::td",
                            )
                        )
                    ).text
                    year_elements = wait.until(
                        EC.presence_of_all_elements_located(
                            (
                                By.XPATH,
                                "//td[contains(., 'Ano da Prestação de Contas:')]",
                            )
                        )
                    )
                    paid_years = [
                        re.search(
                            r'Ano da Prestação de Contas:\s*(\d{4})', el.text
                        ).group(1)
                        for el in year_elements
                    ]
                    return {
                        'Code': code,
                        'Status': 'valid',
                        'NIF': nif,
                        'Company': company,
                        'Paid years': ', '.join(paid_years),
                        'Number of paid years': len(paid_years),
                        'Tries': attempts + 1,
                    }

                except TimeoutException:
                    try:
                        en_nif = wait.until(EC.visibility_of_element_located(
                                (
                                    By.XPATH,
                                    "//td[contains(text(), 'NIPC (Collective person/Registration identification number):')]/following-sibling::td",
                                )
                            )
                        ).text
                        if en_nif:
                            return {
                                'Code': code,
                                'Status': 'english',
                                'NIF': en_nif,
                                'Company': 'please check the code',
                                'Tries': attempts + 1,
                                'Error': 'The code is in English',
                            }
                    except TimeoutException:
                        attempts += 1
                        time.sleep(1)
                        continue
                    
            except TimeoutException:
                attempts += 1
                time.sleep(1)
                continue

        except Exception as e:
            last_exception = e
            logger.error(f'Erro inesperado: {str(e)}')
            attempts += 1
            time.sleep(1)

    # If the code get here, is because all attempts failed
    return {
        'Code': code,
        'Status': 'invalid',
        'NIF': '',
        'Company': '',
        'Tries': MAX_RETRIES,
        'Error': str(last_exception)
        if last_exception
        else 'Timeout after 3 tries',
    }