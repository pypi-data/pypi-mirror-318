import unittest
from plapi_string.similarity import levenshtein_distance, jaccard_similarity, cosine_similarity

class TestSimilarity(unittest.TestCase):

    def test_levenshtein_distance(self):
        self.assertEqual(levenshtein_distance("kitten", "sitting"), 3)
        self.assertEqual(levenshtein_distance("flaw", "lawn"), 2)
        self.assertEqual(levenshtein_distance("", ""), 0)
        self.assertEqual(levenshtein_distance("a", ""), 1)
        self.assertEqual(levenshtein_distance("", "a"), 1)
        self.assertEqual(levenshtein_distance("abc", "abc"), 0)

    def test_jaccard_similarity(self):
        self.assertAlmostEqual(jaccard_similarity("abc", "abc"), 1.0)
        self.assertAlmostEqual(jaccard_similarity("abc", "def"), 0.0)
        self.assertAlmostEqual(jaccard_similarity("abc", "ab"), 2/3)
        self.assertAlmostEqual(jaccard_similarity("abc", ""), 0.0)
        self.assertAlmostEqual(jaccard_similarity("", ""), 1.0)

    def test_cosine_similarity(self):
        self.assertAlmostEqual(cosine_similarity("abc", "abc"), 1.0)
        self.assertAlmostEqual(cosine_similarity("abc", "def"), 0.0)
        self.assertAlmostEqual(cosine_similarity("abc", "ab"), 0.8164965809277261)
        self.assertAlmostEqual(cosine_similarity("abc", ""), 0.0)
        self.assertAlmostEqual(cosine_similarity("", ""), 0.0)

if __name__ == '__main__':
    unittest.main()