# -*- coding: utf-8 -*-

from ome.models import *
from ome.components import *

import pytest


@pytest.mark.usefixtures('load_genomes')
class TestWithGenomes():
    def test_genome_genes(self, session):
        assert (session.query(Gene)
                .filter(Gene.bigg_id == 'b0114')
                .count()) == 2


    def test_genome_synonyms_locus_tag(self, session):
        assert (session.query(Synonym)
                .join(DataSource)
                .join(Gene, Gene.id == Synonym.ome_id)
                .filter(DataSource.name == 'locus_tag')
                .filter(Synonym.synonym == 'b0114')
                .filter(Gene.bigg_id == 'b0114')
                .count()) == 2


    def test_genome_synonyms_name(self, session):
        assert (session.query(Synonym)
                .join(DataSource)
                .filter(DataSource.name == 'refseq_name')
                .filter(Synonym.synonym == 'aceE')
                .count()) == 2


    def test_genome_synonyms_synonyms(self, session):
        assert (session.query(Synonym)
                .join(DataSource)
                .filter(DataSource.name == 'refseq_synonym')
                .filter(Synonym.synonym == 'ECK0113')
                .count()) == 2


    def test_genome_synonyms_db_xref(self, session):
        assert (session.query(Synonym)
                .join(DataSource)
                .filter(DataSource.name == 'GI')
                .filter(Synonym.synonym == '16128107')
                .count()) == 2


    def test_genome_synonyms_db_xref_duplicate(self, session):
        # this causes an error when we are not dealing with duplicates correctly
        assert (session.query(Synonym)
                .join(DataSource)
                .filter(DataSource.name == 'tests_dup_syn')
                .filter(Synonym.synonym == 'b0114')
                .count()) == 1


    # only in core.gb:
    def test_genome_synonyms_old_locus_tag(self, session):
        assert (session.query(Synonym)
                .join(DataSource)
                .filter(DataSource.name == 'refseq_old_locus_tag')
                .filter(Synonym.synonym == 'test_b0114')
                .count()) == 1


    # only in core.gb:
    def test_genome_synonyms_orf_id(self, session):
        assert (session.query(Synonym)
                .join(DataSource)
                .filter(DataSource.name == 'refseq_orf_id')
                .filter(Synonym.synonym == 'test_orf')
                .count()) == 1
