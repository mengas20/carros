name = input("whats your name")
cars = ["swift","sandero","laguna"]
print(f"""welcome {name},
to car evaluation website
""")
your_car = input("whats your car")
while your_car not in cars:
    your_car = input("please enter one of these cars = sandero, swift, laguna")
if your_car == "swift" :
    print(f"""Under the hood, the Suzuki Swift Sport is powered by a
     1.4-liter turbocharged engine that delivers 138 horsepower and 170
      lb-ft of torque. This engine is paired with a six-speed manual
       transmission that provides precise and responsive shifting, making 
       it a joy to drive. The car also features a sport-tuned suspension 
       nd upgraded brakes that provide excellent handling and stopping power.""")
elif your_car == "sandero" :
    print(f"""Under the hood, the Dacia Sandero is powered by a .9-liter 
    four-cylinder engine that delivers 90 horsepower and 9 lb-ft of torque.
     This engine is paired with a five-speed manual transmission that provides 
     smooth and responsive shifting, making it a competent performer in
      the city and on the highway.""")
elif your_car == "laguna" :
    print(f"""Under the hood, the 2004 Renault Laguna is available with a
     range of gasoline and diesel engines, including a 1.6-liter, 1.8-liter,
      and 2.0-liter gasoline engines, and a 1.9-liter and 2.2-liter diesel engines.
       These engines are paired with either a five-speed manual or a 
       six-speed automatic transmission, which provides smooth and responsive
        shifting.""")







