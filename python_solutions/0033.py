from fractions import Fraction as frac

sol = frac(1,1)

for denom in range(11,100):
    for numer in range(10, denom):



        fr = frac(numer, denom)



        if numer%10 != 0 and denom%10 != 0: #eliminating trivial ones
            Sdenom = str(denom)
            Snumer = str(numer)
            Sdenom_ori = Sdenom
            Snumer_ori = Snumer


            if Sdenom[0] == Snumer[0]:
                Sdenom = Sdenom[1]
                Snumer = Snumer[1]
            elif Sdenom[1] == Snumer[1]:
                Sdenom = Sdenom[0]
                Snumer = Snumer[0]
            elif Sdenom[0] == Snumer[1]:
                Sdenom = Sdenom[1]
                Snumer = Snumer[0]
            elif Sdenom[1] == Snumer[0]:
                Sdenom = Sdenom[0]
                Snumer = Snumer[1]

            if len(Sdenom)+len(Snumer) == 2:
                if int(Sdenom) != 0:
                    if frac(int(Snumer), int(Sdenom)) == fr:
                        print(fr, "=", int(Snumer_ori), "/", int(Sdenom_ori))
                        sol *= fr


print(sol)

