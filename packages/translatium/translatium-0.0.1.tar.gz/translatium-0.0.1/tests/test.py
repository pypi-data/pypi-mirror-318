from translatium import translatium

translatium.init_translatium('locales/', 'en_US')
translatium.set_language('de_DE')

print(translatium.translation('hello_message'))
