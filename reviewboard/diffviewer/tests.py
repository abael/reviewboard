from reviewboard.diffviewer.processors import (filter_interdiff_opcodes,
                                               merge_adjacent_chunks)
from reviewboard.testing import TestCase
                          ("equal", 0, 6, 2, 8)])
                         [("equal", 0, 4, 0, 4),
                          ("insert", 5, 5, 5, 9),
                          ("equal", 5, 8, 9, 12)])
            self.assertTrue(file.origFile.startswith("%s/orig_src/" %
            self.assertTrue(file.newFile.startswith("%s/new_src/" %
    def test_line_counts(self):
        """Testing DiffParser with insert/delete line counts"""
        diff = (
            '+ This is some line before the change\n'
            '- And another line\n'
            'Index: foo\n'
            '- One last.\n'
            '--- README  123\n'
            '+++ README  (new)\n'
            '@ -1,1 +1,1 @@\n'
            '-blah blah\n'
            '-blah\n'
            '+blah!\n'
            '-blah...\n'
            '+blah?\n'
            '-blah!\n'
            '+blah?!\n')
        files = diffparser.DiffParser(diff).parse()

        self.assertEqual(len(files), 1)
        self.assertEqual(files[0].insert_count, 3)
        self.assertEqual(files[0].delete_count, 4)

class FileDiffMigrationTests(TestCase):
    fixtures = ['test_scmtools']

    def setUp(self):
        self.diff = (
            'diff --git a/README b/README\n'
            'index d6613f5..5b50866 100644\n'
            '--- README\n'
            '+++ README\n'
            '@ -1,1 +1,1 @@\n'
            '-blah blah\n'
            '+blah!\n')
        self.parent_diff = (
            'diff --git a/README b/README\n'
            'index d6613f5..5b50866 100644\n'
            '--- README\n'
            '+++ README\n'
            '@ -1,1 +1,1 @@\n'
            '-blah..\n'
            '+blah blah\n')

        repository = self.create_repository(tool_name='Test')
        diffset = DiffSet.objects.create(name='test',
                                         revision=1,
                                         repository=repository)
        self.filediff = FileDiff(source_file='README',
                                 dest_file='README',
                                 diffset=diffset,
                                 diff64='',
                                 parent_diff64='')

    def test_migration_by_diff(self):
        """Testing FileDiffData migration accessing FileDiff.diff"""
        self.filediff.diff64 = self.diff

        self.assertEqual(self.filediff.diff_hash, None)
        self.assertEqual(self.filediff.parent_diff_hash, None)

        # This should prompt the migration
        diff = self.filediff.diff

        self.assertEqual(self.filediff.parent_diff_hash, None)
        self.assertNotEqual(self.filediff.diff_hash, None)

        self.assertEqual(diff, self.diff)
        self.assertEqual(self.filediff.diff64, '')
        self.assertEqual(self.filediff.diff_hash.binary, self.diff)
        self.assertEqual(self.filediff.diff, diff)
        self.assertEqual(self.filediff.parent_diff, None)
        self.assertEqual(self.filediff.parent_diff_hash, None)

    def test_migration_by_parent_diff(self):
        """Testing FileDiffData migration accessing FileDiff.parent_diff"""
        self.filediff.diff64 = self.diff
        self.filediff.parent_diff64 = self.parent_diff

        self.assertEqual(self.filediff.parent_diff_hash, None)

        # This should prompt the migration
        parent_diff = self.filediff.parent_diff

        self.assertNotEqual(self.filediff.parent_diff_hash, None)

        self.assertEqual(parent_diff, self.parent_diff)
        self.assertEqual(self.filediff.parent_diff64, '')
        self.assertEqual(self.filediff.parent_diff_hash.binary,
                         self.parent_diff)
        self.assertEqual(self.filediff.parent_diff, self.parent_diff)

    def test_migration_by_delete_count(self):
        """Testing FileDiffData migration accessing FileDiff.delete_count"""
        self.filediff.diff64 = self.diff

        self.assertEqual(self.filediff.diff_hash, None)

        # This should prompt the migration
        delete_count = self.filediff.delete_count

        self.assertNotEqual(self.filediff.diff_hash, None)
        self.assertEqual(delete_count, 1)
        self.assertEqual(self.filediff.diff_hash.delete_count, 1)

    def test_migration_by_insert_count(self):
        """Testing FileDiffData migration accessing FileDiff.insert_count"""
        self.filediff.diff64 = self.diff

        self.assertEqual(self.filediff.diff_hash, None)

        # This should prompt the migration
        insert_count = self.filediff.insert_count

        self.assertNotEqual(self.filediff.diff_hash, None)
        self.assertEqual(insert_count, 1)
        self.assertEqual(self.filediff.diff_hash.insert_count, 1)

    def test_migration_by_set_line_counts(self):
        """Testing FileDiffData migration calling FileDiff.set_line_counts"""
        self.filediff.diff64 = self.diff

        self.assertEqual(self.filediff.diff_hash, None)

        # This should prompt the migration, but with our line counts.
        self.filediff.set_line_counts(10, 20)

        self.assertNotEqual(self.filediff.diff_hash, None)
        self.assertEqual(self.filediff.insert_count, 10)
        self.assertEqual(self.filediff.delete_count, 20)
        self.assertEqual(self.filediff.diff_hash.insert_count, 10)
        self.assertEqual(self.filediff.diff_hash.delete_count, 20)


                          '<span class="hl">abc</span>')
                          '<span class="hl">a</span>bc')
        repository = self.create_repository()
        repository = self.create_repository()
            'diff --git a/README b/README\n'
            'index d6613f5..5b50866 100644\n'
            '--- README\n'
            '+++ README\n'
        repository = self.create_repository(tool_name='Test')
            'diff --git a/README b/README\n'
            'index d6613f5..5b50866 100644\n'
            '--- README\n'
            '+++ README\n'
        repository = self.create_repository(tool_name='Test')
            'diff --git a/README b/README\n'
            'index d6613f5..5b50866 100644\n'
            '--- README\n'
            '+++ README\n'
            'diff --git a/README b/README\n'
            'index d6613f4..5b50865 100644\n'
            '--- README\n'
            '+++ README\n'
            'diff --git a/UNUSED b/UNUSED\n'
            'index 1234567..5b50866 100644\n'
            '--- UNUSED\n'
            '+++ UNUSED\n'
        repository = self.create_repository(tool_name='Test')
        self.assertTrue(('/README', 'd6613f4') in saw_file_exists)
        self.assertFalse(('/UNUSED', '1234567') in saw_file_exists)
class ProcessorsTests(TestCase):
    """Unit tests for diff processors."""

    def test_filter_interdiff_opcodes(self):
        """Testing filter_interdiff_opcodes"""
        opcodes = [
            ('insert', 0, 0, 0, 1),
            ('equal', 0, 5, 1, 5),
            ('delete', 5, 10, 5, 5),
            ('equal', 10, 25, 5, 20),
            ('replace', 25, 26, 20, 26),
            ('equal', 26, 40, 26, 40),
            ('insert', 40, 40, 40, 45),
        ]

        # NOTE: Only the "@@" lines in the diff matter below for this
        #       processor, so the rest can be left out.
        orig_diff = '@@ -22,7 +22,7 @@\n'
        new_diff = (
            '@@ -2,11 +2,6 @@\n'
            '@@ -22,7 +22,7 @@\n'
        )

        new_opcodes = list(filter_interdiff_opcodes(opcodes, orig_diff,
                                                    new_diff))

        self.assertEqual(new_opcodes, [
            ('equal', 0, 0, 0, 1),
            ('equal', 0, 5, 1, 5),
            ('delete', 5, 10, 5, 5),
            ('equal', 10, 25, 5, 20),
            ('replace', 25, 26, 20, 26),
            ('equal', 26, 40, 26, 40),
            ('equal', 40, 40, 40, 45),
        ])

    def test_filter_interdiff_opcodes_with_inserts_right(self):
        """Testing filter_interdiff_opcodes with inserts on the right"""
        # These opcodes were taken from the r1-r2 interdiff at
        # http://reviews.reviewboard.org/r/4221/
        opcodes = [
            ('equal', 0, 141, 0, 141),
            ('replace', 141, 142, 141, 142),
            ('insert', 142, 142, 142, 144),
            ('equal', 142, 165, 144, 167),
            ('replace', 165, 166, 167, 168),
            ('insert', 166, 166, 168, 170),
            ('equal', 166, 190, 170, 194),
            ('insert', 190, 190, 194, 197),
            ('equal', 190, 232, 197, 239),
        ]

        # NOTE: Only the "@@" lines in the diff matter below for this
        #       processor, so the rest can be left out.
        orig_diff = '@@ -0,0 +1,232 @@\n'
        new_diff = '@@ -0,0 +1,239 @@\n'

        new_opcodes = list(filter_interdiff_opcodes(opcodes, orig_diff,
                                                    new_diff))

        self.assertEqual(new_opcodes, [
            ('equal', 0, 141, 0, 141),
            ('replace', 141, 142, 141, 142),
            ('insert', 142, 142, 142, 144),
            ('equal', 142, 165, 144, 167),
            ('replace', 165, 166, 167, 168),
            ('insert', 166, 166, 168, 170),
            ('equal', 166, 190, 170, 194),
            ('insert', 190, 190, 194, 197),
            ('equal', 190, 232, 197, 239),
        ])

    def test_merge_adjacent_chunks(self):
        """Testing merge_adjacent_chunks"""
        opcodes = [
            ('equal', 0, 0, 0, 1),
            ('equal', 0, 5, 1, 5),
            ('delete', 5, 10, 5, 5),
            ('equal', 10, 25, 5, 20),
            ('replace', 25, 26, 20, 26),
            ('equal', 26, 40, 26, 40),
            ('equal', 40, 40, 40, 45),
        ]

        new_opcodes = list(merge_adjacent_chunks(opcodes))

        self.assertEqual(new_opcodes, [
            ('equal', 0, 5, 0, 5),
            ('delete', 5, 10, 5, 5),
            ('equal', 10, 25, 5, 20),
            ('replace', 25, 26, 20, 26),
            ('equal', 26, 40, 26, 45),
        ])


            'newfile': True,
            'interfilediff': None,
            'filediff': FileDiff(),