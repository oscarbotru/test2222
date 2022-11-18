DRIVER_IDs = [36608123, 30487162, 90482770]

def reward_calc():

    def inner(price):
        inner.total_reward += price * inner.percentage
        inner.percentage += 0.01

    inner.total_reward = 0
    inner.percentage = 0.01

    return inner


driver_func = {36608123: reward_calc()}

driver_func[36608123](200)
print(driver_func[36608123].total_reward)

driver_func[36608123](200)
print(driver_func[36608123].total_reward)
