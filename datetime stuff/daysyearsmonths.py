from datetime import timedelta
year = timedelta(days=365)
ten_years = 10 * year
#ten_years
#datetime.timedelta(days=3650)


ten_years.days // 365
nine_years = ten_years - year
#nine_years
#datetime.timedelta(days=3285)

three_years = nine_years // 3
three_years, three_years.days // 365
