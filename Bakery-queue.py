Bakery_queue=['ali','atefeh','reza','homa','amir','fatemeh']

first_aghazade = input('whats your name?')
first_aghazade_place = int(input('whats place do you want?')) 

second_aghazade = input('whats your name?')
second_aghazade_place = int(input('whats place do you want?'))

third_aghazade =input('whats your name?')
third_aghazade_place = int(input('whats place do you want?'))

Bakery_queue.insert(first_aghazade_place-1, first_aghazade)
Bakery_queue.insert(second_aghazade_place-1, second_aghazade)
Bakery_queue.insert(third_aghazade_place-1, third_aghazade)

print(Bakery_queue)

