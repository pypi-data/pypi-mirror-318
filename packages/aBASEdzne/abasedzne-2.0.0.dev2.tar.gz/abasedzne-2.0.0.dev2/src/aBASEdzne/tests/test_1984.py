import unittest


class Test1984(unittest.TestCase):
    def test_1984(self):
        self.assertEqual(2 + 2, 4, "Ignorance is Strength")


if __name__ == "__main__":
    unittest.main()


# python3 aBASE.py --hchain "G4:G300" --heavykeys "H3:W3" --kchain "Y4:Y300" --kappakeys "Z3:AM3"  --lchain "AO4:AO300" --lambdakeys "AP3:BC3" --dataprefix=/data/SeqData/ /data/aBASE-113-input.xlsx /results/aBASE-output.xlsm
# echo "aBASE validation complete."
