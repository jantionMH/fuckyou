


def oneclick_bet(self):
    self.s(text='一键投注').click()
    bet_amount=self.s(resourceId='com.yy.sport:id/tv_amount').get_text()
    current_amount=self.s(resourceId='com.yy.sport:id/tv_account_balance').get_text()

    cu_amount=current_amount.replace(',','')
    a=cu_amount.split('.')[0]+'.'+cu_amount.split('.')[1][:2]
    self.s(text='确定').click()
    return  [bet_amount,a]


def add_list_bet(self):

    self.s(text='确认下注').click()
    bet_amount = self.s(resourceId='com.yy.sport:id/tv_amount').get_text()
    current_amount = self.s(resourceId='com.yy.sport:id/tv_account_balance').get_text()
    cu_amount = current_amount.replace(',', '')
    a = cu_amount.split('.')[0] + '.' + cu_amount.split('.')[1][:2]
    self.s(text='确定').click()
    return [bet_amount, a]