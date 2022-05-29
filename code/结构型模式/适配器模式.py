from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


class Alipay(Payment):
    def pay(self, money):
        print(f"支付宝支付{money}")


class Wechatpay(Payment):
    def pay(self, money):
        print(f"微信支付{money}")


class BankPay:
    def cost(self, money):
        print(f"银联支付{money}")


class ApplePay:
    def cost(self, money):
        print(f"苹果支付{money}")


# 类适配器： 继承
# 以上的接口不兼容，使用适配器实现接口统一
class NewBankPay(Payment, BankPay):
    def pay(self, money):
        self.cost(money)


# 对象适配器
class PaymentAdater(Payment):
    def __init__(self, payment) -> None:
        self.payment = payment

    def pay(self, money):
        self.payment.cost(money)


# 组合
# p = NewBankPay()
# p.pay(100)

p = PaymentAdater(ApplePay())
p.pay(100)

p = PaymentAdater(BankPay())
p.pay(100)

p = Wechatpay()
p.pay(100)
