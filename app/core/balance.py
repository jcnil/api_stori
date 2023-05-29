import glob
import pandas as pd


class AccountBalance:
    @staticmethod
    def account_balance(request: dict) -> dict:
        filepath = glob.glob(f"**/{request.get('filename')}", recursive=True)
        df = pd.read_csv(filepath[0],  sep=',',  comment='#')

        df['Month_num'] = df.Date.str.split('/').str.get(0)
        df['Day'] = df.Date.str.split('/').str.get(1)

        total = df['Transaction'].sum()

        debit_sum = df[df['Transaction'] > 0].sum()
        credit_sum = df[df['Transaction'] < 0].sum()

        count_debit = df[df['Transaction'] > 0].count()
        count_credit = df[df['Transaction'] < 0].count()

        count = df.groupby('Month_num').nunique()

        debit = debit_sum['Transaction']/count_debit['Transaction']
        credit = credit_sum['Transaction']/count_credit['Transaction']

        months = count.index

        n_months = []
        for m in list(months):
            if m == '1':
                n_months.append('January')
            elif m == '2':
                n_months.append('February')
            elif m == '3':
                n_months.append('March')
            elif m == '4':
                n_months.append('April')
            elif m == '5':
                n_months.append('May')
            elif m == '6':
                n_months.append('June')
            elif m == '7':
                n_months.append('July')
            elif m == '8':
                n_months.append('August')
            elif m == '9':
                n_months.append('September')
            elif m == '10':
                n_months.append('October')
            elif m == '11':
                n_months.append('November')
            elif m == '12':
                n_months.append('December')

        return {
            "total": "{:.2f}".format(total),
            "debit": "{:.2f}".format(debit),
            "credit": "{:.2f}".format(credit),
            "months": n_months,
            "move": list(count['Transaction'])
        }
