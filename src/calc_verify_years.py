def verify_years(paid_years, selected_year):
    if not paid_years:
        return []
    primeiro_ano = min(map(int, paid_years))
    return sorted(
        set(range(primeiro_ano, int(selected_year) + 1))
        - set(map(int, paid_years))
    )
