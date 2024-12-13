from scr import get_mask_card_number, get_mask_account


def mask_account_card(*infa):
    infa = list(infa)
    if infa[0] != 'Счёт' or infa[0] != 'Счет':
        infa[1] = get_mask_card_number(str(infa[1]))
        return f'{infa[0]} {infa[1]}'
    infa[1] = get_mask_account(str(infa[1]))
    return f'{infa[0]} {infa[1]}'


print(mask_account_card("Visa Platinum", 7000792289606361))
print(mask_account_card('Счет', 73654108430135874305))