from scr import get_mask_card_number, get_mask_account


def mask_account_card(infa: str) -> str:
    lis_ = infa.split()
    if 'счет' in ' '.join(lis_[:-1]).lower():
        lis_[-1] = get_mask_account(lis_[-1])
        return ' '.join(lis_)
    lis_[1] = get_mask_card_number(lis_[-1])
    return ' '.join(lis_)


def get_date(infa: str) -> str:
    data = infa[:10].split("-")
    return f"{data[2]}-{data[1]}-{data[0]}"


print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Счет 73654108430135874305"))
print(get_date("2024-12-10T02:26:18.671407"))
