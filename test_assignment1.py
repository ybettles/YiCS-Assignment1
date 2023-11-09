import assignment1

class TestClass:

    def test_clean_up(self):
        assert assignment1.clean_up() == ('Michael Adam Smith\n'
                                          'Amy Jones\n'
                                          'Mary Ann Smith\n'
                                          'Mark Ant Sweepy\n'
                                          'Jarryd Stephenson\n'
                                          'Hannah Chetty\n'
                                          'Anya Gonzalez\n'
                                          'Jon Stewart\n'
                                          'Jenny Squi\n')

    def test_build_id(self):
        assert assignment1.build_id() == ["mas", "axj", "mas", "mas", "jxs", "hxc", "axg", "jxs", "jxs"]

    def test_validate_passwordShort(self):
        assert assignment1.validate_password("asdABC") == ['TOO SHORT']

    def test_validate_password2(self):
        assert assignment1.validate_password("abcde12345678ABC") == ['TOO LONG']

    def test_validate_password3(self):
        assert assignment1.validate_password("s@dmeA123") == ['WRONG CHARACTERS']

    def test_validate_passwordMixed_case(self):
        assert assignment1.validate_password("ABCDEFGLK") == ['NOT MIXED CASE']

    def test_validate_password5(self):
        assert assignment1.validate_password("12345678aza") == ['NOT MIXED CASE', 'LEADING DIGIT']

    def test_validate_password6(self):
        assert assignment1.validate_password("Password123") == ['CANNOT MAKE USE OF THIS PASSWORD']

    def test_create_unique(self):
        id_list = ["mas", "axj", "mas", "mas", "jxs", "hxc", "axg", "jxs", "jxs"]
        assert assignment1.create_unique(id_list).count('mas0001') > 0
        assert assignment1.create_unique(id_list).count('mas0002') > 0
        assert assignment1.create_unique(id_list).count('jxs0001') > 0
        assert assignment1.create_unique(id_list).count('jxs0002') > 0


    def test_create_short_address(self):
        assert assignment1.create_short_address() == [['2 Smith street', 'B312'], ['25 Eddie drive', 'C912WW'],
                                                      ['1 Short street', 'C112GH'], ['5 Long street', 'L236QA'],
                                                      ['122 Abex road', 'A432LK'], ['55 Kings street', 'M457JK'],
                                                      ['2 Canal street', 'MWE2KL'], ['234 Bold street', 'L128JK'],
                                                      ['5 Abbey road', '1163JK']]

    def test_validate_pcode(self):
        split_addrs = ['2 Smith street', 'B312'], ['25 Eddie drive', 'C912WW'], ['1 Short street', 'C112GH'], \
            ['5 Long street', 'L236QA'], ['122 Abex road', 'A432LK'], ['55 Kings street', 'M457JK'], \
            ['2 Canal street', 'MWE2KL'], ['234 Bold street', 'L128JK'], ['5 Abbey road', '1163JK']
        assert assignment1.validate_pcode(split_addrs) == [0, 'False', 'False', 'False', 'False', \
                                                           1, 'True', 'True', 'True', 'True', \
                                                           2, 'True', 'True', 'True', 'True', \
                                                           3, 'True', 'True', 'True', 'True', \
                                                           4, 'True', 'True', 'True', 'True', \
                                                           5, 'True', 'True', 'True', 'True', \
                                                           6, 'True', 'True', 'False', 'True', \
                                                           7, 'True', 'True', 'True', 'True', \
                                                           8, 'True', 'False', 'True', 'True']

    def test_ids_addrs(self):
        short_addr = [['2 Smith street', 'B312AB'], ['25 Eddie drive', 'C912WW'], ['1 Short street', 'C112GH'],
                      ['5 Long street', 'L236QA'], \
                      ['122 Abex road', 'A432JH'], ['55 Kings street', 'M432JK'], ['2 Canal street', 'M222KL'],
                      ['234 Bold street', 'L128JK'], \
                      ['5 Abbey road', '1P63JA']]
        assert assignment1.ids_addrs(short_addr) == {'axg0000': ['122 Abex road', 'A432JH'],
                                                     'axj0000': ['25 Eddie drive', 'C912WW'],
                                                     'hxc0000': ['5 Long street', 'L236QA'],
                                                     'jxs0000': ['1 Short street', 'C112GH'],
                                                     'jxs0001': ['234 Bold street', 'L128JK'],
                                                     'jxs0002': ['5 Abbey road', '1P63JA'],
                                                     'mas0000': ['2 Smith street', 'B312AB'],
                                                     'mas0001': ['55 Kings street', 'M432JK'],
                                                     'mas0002': ['2 Canal street', 'M222KL']}
