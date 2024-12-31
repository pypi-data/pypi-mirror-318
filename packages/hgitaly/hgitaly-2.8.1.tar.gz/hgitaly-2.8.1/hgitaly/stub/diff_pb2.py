# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: diff.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import lint_pb2 as lint__pb2
from . import shared_pb2 as shared__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ndiff.proto\x12\x06gitaly\x1a\nlint.proto\x1a\x0cshared.proto\"\xd8\x06\n\x11\x43ommitDiffRequest\x12,\n\nrepository\x18\x01 \x01(\x0b\x32\x12.gitaly.RepositoryB\x04\x98\xc6,\x01\x12\x16\n\x0eleft_commit_id\x18\x02 \x01(\t\x12\x17\n\x0fright_commit_id\x18\x03 \x01(\t\x12\r\n\x05paths\x18\x05 \x03(\x0c\x12\x16\n\x0e\x63ollapse_diffs\x18\x06 \x01(\x08\x12\x16\n\x0e\x65nforce_limits\x18\x07 \x01(\x08\x12\x11\n\tmax_files\x18\x08 \x01(\x05\x12\x11\n\tmax_lines\x18\t \x01(\x05\x12\x11\n\tmax_bytes\x18\n \x01(\x05\x12\x17\n\x0fmax_patch_bytes\x18\x0e \x01(\x05\x12\x16\n\x0esafe_max_files\x18\x0b \x01(\x05\x12\x16\n\x0esafe_max_lines\x18\x0c \x01(\x05\x12\x16\n\x0esafe_max_bytes\x18\r \x01(\x05\x12\x35\n\tdiff_mode\x18\x0f \x01(\x0e\x32\".gitaly.CommitDiffRequest.DiffMode\x12h\n\"max_patch_bytes_for_file_extension\x18\x10 \x03(\x0b\x32<.gitaly.CommitDiffRequest.MaxPatchBytesForFileExtensionEntry\x12G\n\x12whitespace_changes\x18\x11 \x01(\x0e\x32+.gitaly.CommitDiffRequest.WhitespaceChanges\x12\x19\n\x11\x63ollect_all_paths\x18\x12 \x01(\x08\x1a\x44\n\"MaxPatchBytesForFileExtensionEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\"%\n\x08\x44iffMode\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x0c\n\x08WORDDIFF\x10\x01\"y\n\x11WhitespaceChanges\x12\"\n\x1eWHITESPACE_CHANGES_UNSPECIFIED\x10\x00\x12\x1d\n\x19WHITESPACE_CHANGES_IGNORE\x10\x01\x12!\n\x1dWHITESPACE_CHANGES_IGNORE_ALL\x10\x02J\x04\x08\x04\x10\x05R\x18ignore_whitespace_change\"\xff\x01\n\x12\x43ommitDiffResponse\x12\x11\n\tfrom_path\x18\x01 \x01(\x0c\x12\x0f\n\x07to_path\x18\x02 \x01(\x0c\x12\x0f\n\x07\x66rom_id\x18\x03 \x01(\t\x12\r\n\x05to_id\x18\x04 \x01(\t\x12\x10\n\x08old_mode\x18\x05 \x01(\x05\x12\x10\n\x08new_mode\x18\x06 \x01(\x05\x12\x0e\n\x06\x62inary\x18\x07 \x01(\x08\x12\x16\n\x0eraw_patch_data\x18\t \x01(\x0c\x12\x14\n\x0c\x65nd_of_patch\x18\n \x01(\x08\x12\x17\n\x0foverflow_marker\x18\x0b \x01(\x08\x12\x11\n\tcollapsed\x18\x0c \x01(\x08\x12\x11\n\ttoo_large\x18\r \x01(\x08J\x04\x08\x08\x10\t\"\x82\x01\n\x12\x43ommitDeltaRequest\x12,\n\nrepository\x18\x01 \x01(\x0b\x32\x12.gitaly.RepositoryB\x04\x98\xc6,\x01\x12\x16\n\x0eleft_commit_id\x18\x02 \x01(\t\x12\x17\n\x0fright_commit_id\x18\x03 \x01(\t\x12\r\n\x05paths\x18\x04 \x03(\x0c\"u\n\x0b\x43ommitDelta\x12\x11\n\tfrom_path\x18\x01 \x01(\x0c\x12\x0f\n\x07to_path\x18\x02 \x01(\x0c\x12\x0f\n\x07\x66rom_id\x18\x03 \x01(\t\x12\r\n\x05to_id\x18\x04 \x01(\t\x12\x10\n\x08old_mode\x18\x05 \x01(\x05\x12\x10\n\x08new_mode\x18\x06 \x01(\x05\":\n\x13\x43ommitDeltaResponse\x12#\n\x06\x64\x65ltas\x18\x01 \x03(\x0b\x32\x13.gitaly.CommitDelta\"o\n\x0eRawDiffRequest\x12,\n\nrepository\x18\x01 \x01(\x0b\x32\x12.gitaly.RepositoryB\x04\x98\xc6,\x01\x12\x16\n\x0eleft_commit_id\x18\x02 \x01(\t\x12\x17\n\x0fright_commit_id\x18\x03 \x01(\t\"\x1f\n\x0fRawDiffResponse\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"p\n\x0fRawPatchRequest\x12,\n\nrepository\x18\x01 \x01(\x0b\x32\x12.gitaly.RepositoryB\x04\x98\xc6,\x01\x12\x16\n\x0eleft_commit_id\x18\x02 \x01(\t\x12\x17\n\x0fright_commit_id\x18\x03 \x01(\t\" \n\x10RawPatchResponse\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"q\n\x10\x44iffStatsRequest\x12,\n\nrepository\x18\x01 \x01(\x0b\x32\x12.gitaly.RepositoryB\x04\x98\xc6,\x01\x12\x16\n\x0eleft_commit_id\x18\x02 \x01(\t\x12\x17\n\x0fright_commit_id\x18\x03 \x01(\t\"Q\n\tDiffStats\x12\x0c\n\x04path\x18\x01 \x01(\x0c\x12\x11\n\tadditions\x18\x02 \x01(\x05\x12\x11\n\tdeletions\x18\x03 \x01(\x05\x12\x10\n\x08old_path\x18\x04 \x01(\x0c\"5\n\x11\x44iffStatsResponse\x12 \n\x05stats\x18\x01 \x03(\x0b\x32\x11.gitaly.DiffStats\"\xda\x05\n\x17\x46indChangedPathsRequest\x12,\n\nrepository\x18\x01 \x01(\x0b\x32\x12.gitaly.RepositoryB\x04\x98\xc6,\x01\x12\x13\n\x07\x63ommits\x18\x02 \x03(\tB\x02\x18\x01\x12\x39\n\x08requests\x18\x03 \x03(\x0b\x32\'.gitaly.FindChangedPathsRequest.Request\x12S\n\x16merge_commit_diff_mode\x18\x04 \x01(\x0e\x32\x33.gitaly.FindChangedPathsRequest.MergeCommitDiffMode\x12\x14\n\x0c\x66ind_renames\x18\x05 \x01(\x08\x1a\xc2\x02\n\x07Request\x12K\n\x0ctree_request\x18\x01 \x01(\x0b\x32\x33.gitaly.FindChangedPathsRequest.Request.TreeRequestH\x00\x12O\n\x0e\x63ommit_request\x18\x02 \x01(\x0b\x32\x35.gitaly.FindChangedPathsRequest.Request.CommitRequestH\x00\x1a\x46\n\x0bTreeRequest\x12\x1a\n\x12left_tree_revision\x18\x01 \x01(\t\x12\x1b\n\x13right_tree_revision\x18\x02 \x01(\t\x1aI\n\rCommitRequest\x12\x17\n\x0f\x63ommit_revision\x18\x01 \x01(\t\x12\x1f\n\x17parent_commit_revisions\x18\x02 \x03(\tB\x06\n\x04type\"\x90\x01\n\x13MergeCommitDiffMode\x12&\n\"MERGE_COMMIT_DIFF_MODE_UNSPECIFIED\x10\x00\x12)\n%MERGE_COMMIT_DIFF_MODE_INCLUDE_MERGES\x10\x01\x12&\n\"MERGE_COMMIT_DIFF_MODE_ALL_PARENTS\x10\x02\"?\n\x18\x46indChangedPathsResponse\x12#\n\x05paths\x18\x01 \x03(\x0b\x32\x14.gitaly.ChangedPaths\"\x83\x02\n\x0c\x43hangedPaths\x12\x0c\n\x04path\x18\x01 \x01(\x0c\x12+\n\x06status\x18\x02 \x01(\x0e\x32\x1b.gitaly.ChangedPaths.Status\x12\x10\n\x08old_mode\x18\x03 \x01(\x05\x12\x10\n\x08new_mode\x18\x04 \x01(\x05\x12\x13\n\x0bold_blob_id\x18\x05 \x01(\t\x12\x13\n\x0bnew_blob_id\x18\x06 \x01(\t\x12\x10\n\x08old_path\x18\x07 \x01(\x0c\"X\n\x06Status\x12\t\n\x05\x41\x44\x44\x45\x44\x10\x00\x12\x0c\n\x08MODIFIED\x10\x01\x12\x0b\n\x07\x44\x45LETED\x10\x02\x12\x0f\n\x0bTYPE_CHANGE\x10\x03\x12\n\n\x06\x43OPIED\x10\x04\x12\x0b\n\x07RENAMED\x10\x05\"m\n\x11GetPatchIDRequest\x12,\n\nrepository\x18\x01 \x01(\x0b\x32\x12.gitaly.RepositoryB\x04\x98\xc6,\x01\x12\x14\n\x0cold_revision\x18\x02 \x01(\x0c\x12\x14\n\x0cnew_revision\x18\x03 \x01(\x0c\"&\n\x12GetPatchIDResponse\x12\x10\n\x08patch_id\x18\x01 \x01(\t\"+\n\tRangePair\x12\x0e\n\x06range1\x18\x01 \x01(\t\x12\x0e\n\x06range2\x18\x02 \x01(\t\"+\n\rRevisionRange\x12\x0c\n\x04rev1\x18\x01 \x01(\t\x12\x0c\n\x04rev2\x18\x02 \x01(\t\"=\n\x11\x42\x61seWithRevisions\x12\x0c\n\x04\x62\x61se\x18\x01 \x01(\t\x12\x0c\n\x04rev1\x18\x02 \x01(\t\x12\x0c\n\x04rev2\x18\x03 \x01(\t\"\xe5\x01\n\x13RawRangeDiffRequest\x12,\n\nrepository\x18\x01 \x01(\x0b\x32\x12.gitaly.RepositoryB\x04\x98\xc6,\x01\x12\'\n\nrange_pair\x18\x02 \x01(\x0b\x32\x11.gitaly.RangePairH\x00\x12/\n\x0erevision_range\x18\x03 \x01(\x0b\x32\x15.gitaly.RevisionRangeH\x00\x12\x38\n\x13\x62\x61se_with_revisions\x18\x04 \x01(\x0b\x32\x19.gitaly.BaseWithRevisionsH\x00\x42\x0c\n\nrange_spec\"$\n\x14RawRangeDiffResponse\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"\xe2\x01\n\x10RangeDiffRequest\x12,\n\nrepository\x18\x01 \x01(\x0b\x32\x12.gitaly.RepositoryB\x04\x98\xc6,\x01\x12\'\n\nrange_pair\x18\x02 \x01(\x0b\x32\x11.gitaly.RangePairH\x00\x12/\n\x0erevision_range\x18\x03 \x01(\x0b\x32\x15.gitaly.RevisionRangeH\x00\x12\x38\n\x13\x62\x61se_with_revisions\x18\x04 \x01(\x0b\x32\x19.gitaly.BaseWithRevisionsH\x00\x42\x0c\n\nrange_spec\"\xc4\x02\n\x11RangeDiffResponse\x12\x16\n\x0e\x66rom_commit_id\x18\x01 \x01(\t\x12\x14\n\x0cto_commit_id\x18\x02 \x01(\t\x12\x38\n\ncomparison\x18\x03 \x01(\x0e\x32$.gitaly.RangeDiffResponse.Comparator\x12\x1c\n\x14\x63ommit_message_title\x18\x07 \x01(\t\x12\x12\n\npatch_data\x18\x08 \x01(\x0c\x12\x14\n\x0c\x65nd_of_patch\x18\t \x01(\x08\"\x7f\n\nComparator\x12 \n\x1c\x43OMPARATOR_EQUAL_UNSPECIFIED\x10\x00\x12\x1b\n\x17\x43OMPARATOR_GREATER_THAN\x10\x01\x12\x18\n\x14\x43OMPARATOR_LESS_THAN\x10\x02\x12\x18\n\x14\x43OMPARATOR_NOT_EQUAL\x10\x03\"\xf9\x03\n\x10\x44iffBlobsRequest\x12,\n\nrepository\x18\x01 \x01(\x0b\x32\x12.gitaly.RepositoryB\x04\x98\xc6,\x01\x12\x35\n\nblob_pairs\x18\x02 \x03(\x0b\x32!.gitaly.DiffBlobsRequest.BlobPair\x12\x34\n\tdiff_mode\x18\x03 \x01(\x0e\x32!.gitaly.DiffBlobsRequest.DiffMode\x12\x46\n\x12whitespace_changes\x18\x04 \x01(\x0e\x32*.gitaly.DiffBlobsRequest.WhitespaceChanges\x12\x19\n\x11patch_bytes_limit\x18\x05 \x01(\x05\x1a\x31\n\x08\x42lobPair\x12\x11\n\tleft_blob\x18\x01 \x01(\x0c\x12\x12\n\nright_blob\x18\x02 \x01(\x0c\"9\n\x08\x44iffMode\x12\x19\n\x15\x44IFF_MODE_UNSPECIFIED\x10\x00\x12\x12\n\x0e\x44IFF_MODE_WORD\x10\x01\"y\n\x11WhitespaceChanges\x12\"\n\x1eWHITESPACE_CHANGES_UNSPECIFIED\x10\x00\x12\x1d\n\x19WHITESPACE_CHANGES_IGNORE\x10\x01\x12!\n\x1dWHITESPACE_CHANGES_IGNORE_ALL\x10\x02\"\xeb\x01\n\x11\x44iffBlobsResponse\x12\x14\n\x0cleft_blob_id\x18\x01 \x01(\t\x12\x15\n\rright_blob_id\x18\x02 \x01(\t\x12\r\n\x05patch\x18\x03 \x01(\x0c\x12\x30\n\x06status\x18\x04 \x01(\x0e\x32 .gitaly.DiffBlobsResponse.Status\x12\x0e\n\x06\x62inary\x18\x05 \x01(\x08\x12\x1e\n\x16over_patch_bytes_limit\x18\x06 \x01(\x08\"8\n\x06Status\x12\x15\n\x11STATUS_INCOMPLETE\x10\x00\x12\x17\n\x13STATUS_END_OF_PATCH\x10\x01\x32\xa4\x06\n\x0b\x44iffService\x12M\n\nCommitDiff\x12\x19.gitaly.CommitDiffRequest\x1a\x1a.gitaly.CommitDiffResponse\"\x06\xfa\x97(\x02\x08\x02\x30\x01\x12P\n\x0b\x43ommitDelta\x12\x1a.gitaly.CommitDeltaRequest\x1a\x1b.gitaly.CommitDeltaResponse\"\x06\xfa\x97(\x02\x08\x02\x30\x01\x12\x44\n\x07RawDiff\x12\x16.gitaly.RawDiffRequest\x1a\x17.gitaly.RawDiffResponse\"\x06\xfa\x97(\x02\x08\x02\x30\x01\x12G\n\x08RawPatch\x12\x17.gitaly.RawPatchRequest\x1a\x18.gitaly.RawPatchResponse\"\x06\xfa\x97(\x02\x08\x02\x30\x01\x12J\n\tDiffStats\x12\x18.gitaly.DiffStatsRequest\x1a\x19.gitaly.DiffStatsResponse\"\x06\xfa\x97(\x02\x08\x02\x30\x01\x12_\n\x10\x46indChangedPaths\x12\x1f.gitaly.FindChangedPathsRequest\x1a .gitaly.FindChangedPathsResponse\"\x06\xfa\x97(\x02\x08\x02\x30\x01\x12K\n\nGetPatchID\x12\x19.gitaly.GetPatchIDRequest\x1a\x1a.gitaly.GetPatchIDResponse\"\x06\xfa\x97(\x02\x08\x02\x12S\n\x0cRawRangeDiff\x12\x1b.gitaly.RawRangeDiffRequest\x1a\x1c.gitaly.RawRangeDiffResponse\"\x06\xfa\x97(\x02\x08\x02\x30\x01\x12J\n\tRangeDiff\x12\x18.gitaly.RangeDiffRequest\x1a\x19.gitaly.RangeDiffResponse\"\x06\xfa\x97(\x02\x08\x02\x30\x01\x12J\n\tDiffBlobs\x12\x18.gitaly.DiffBlobsRequest\x1a\x19.gitaly.DiffBlobsResponse\"\x06\xfa\x97(\x02\x08\x02\x30\x01\x42\x34Z2gitlab.com/gitlab-org/gitaly/v16/proto/go/gitalypbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'diff_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z2gitlab.com/gitlab-org/gitaly/v16/proto/go/gitalypb'
  _COMMITDIFFREQUEST_MAXPATCHBYTESFORFILEEXTENSIONENTRY._options = None
  _COMMITDIFFREQUEST_MAXPATCHBYTESFORFILEEXTENSIONENTRY._serialized_options = b'8\001'
  _COMMITDIFFREQUEST.fields_by_name['repository']._options = None
  _COMMITDIFFREQUEST.fields_by_name['repository']._serialized_options = b'\230\306,\001'
  _COMMITDELTAREQUEST.fields_by_name['repository']._options = None
  _COMMITDELTAREQUEST.fields_by_name['repository']._serialized_options = b'\230\306,\001'
  _RAWDIFFREQUEST.fields_by_name['repository']._options = None
  _RAWDIFFREQUEST.fields_by_name['repository']._serialized_options = b'\230\306,\001'
  _RAWPATCHREQUEST.fields_by_name['repository']._options = None
  _RAWPATCHREQUEST.fields_by_name['repository']._serialized_options = b'\230\306,\001'
  _DIFFSTATSREQUEST.fields_by_name['repository']._options = None
  _DIFFSTATSREQUEST.fields_by_name['repository']._serialized_options = b'\230\306,\001'
  _FINDCHANGEDPATHSREQUEST.fields_by_name['repository']._options = None
  _FINDCHANGEDPATHSREQUEST.fields_by_name['repository']._serialized_options = b'\230\306,\001'
  _FINDCHANGEDPATHSREQUEST.fields_by_name['commits']._options = None
  _FINDCHANGEDPATHSREQUEST.fields_by_name['commits']._serialized_options = b'\030\001'
  _GETPATCHIDREQUEST.fields_by_name['repository']._options = None
  _GETPATCHIDREQUEST.fields_by_name['repository']._serialized_options = b'\230\306,\001'
  _RAWRANGEDIFFREQUEST.fields_by_name['repository']._options = None
  _RAWRANGEDIFFREQUEST.fields_by_name['repository']._serialized_options = b'\230\306,\001'
  _RANGEDIFFREQUEST.fields_by_name['repository']._options = None
  _RANGEDIFFREQUEST.fields_by_name['repository']._serialized_options = b'\230\306,\001'
  _DIFFBLOBSREQUEST.fields_by_name['repository']._options = None
  _DIFFBLOBSREQUEST.fields_by_name['repository']._serialized_options = b'\230\306,\001'
  _DIFFSERVICE.methods_by_name['CommitDiff']._options = None
  _DIFFSERVICE.methods_by_name['CommitDiff']._serialized_options = b'\372\227(\002\010\002'
  _DIFFSERVICE.methods_by_name['CommitDelta']._options = None
  _DIFFSERVICE.methods_by_name['CommitDelta']._serialized_options = b'\372\227(\002\010\002'
  _DIFFSERVICE.methods_by_name['RawDiff']._options = None
  _DIFFSERVICE.methods_by_name['RawDiff']._serialized_options = b'\372\227(\002\010\002'
  _DIFFSERVICE.methods_by_name['RawPatch']._options = None
  _DIFFSERVICE.methods_by_name['RawPatch']._serialized_options = b'\372\227(\002\010\002'
  _DIFFSERVICE.methods_by_name['DiffStats']._options = None
  _DIFFSERVICE.methods_by_name['DiffStats']._serialized_options = b'\372\227(\002\010\002'
  _DIFFSERVICE.methods_by_name['FindChangedPaths']._options = None
  _DIFFSERVICE.methods_by_name['FindChangedPaths']._serialized_options = b'\372\227(\002\010\002'
  _DIFFSERVICE.methods_by_name['GetPatchID']._options = None
  _DIFFSERVICE.methods_by_name['GetPatchID']._serialized_options = b'\372\227(\002\010\002'
  _DIFFSERVICE.methods_by_name['RawRangeDiff']._options = None
  _DIFFSERVICE.methods_by_name['RawRangeDiff']._serialized_options = b'\372\227(\002\010\002'
  _DIFFSERVICE.methods_by_name['RangeDiff']._options = None
  _DIFFSERVICE.methods_by_name['RangeDiff']._serialized_options = b'\372\227(\002\010\002'
  _DIFFSERVICE.methods_by_name['DiffBlobs']._options = None
  _DIFFSERVICE.methods_by_name['DiffBlobs']._serialized_options = b'\372\227(\002\010\002'
  _globals['_COMMITDIFFREQUEST']._serialized_start=49
  _globals['_COMMITDIFFREQUEST']._serialized_end=905
  _globals['_COMMITDIFFREQUEST_MAXPATCHBYTESFORFILEEXTENSIONENTRY']._serialized_start=643
  _globals['_COMMITDIFFREQUEST_MAXPATCHBYTESFORFILEEXTENSIONENTRY']._serialized_end=711
  _globals['_COMMITDIFFREQUEST_DIFFMODE']._serialized_start=713
  _globals['_COMMITDIFFREQUEST_DIFFMODE']._serialized_end=750
  _globals['_COMMITDIFFREQUEST_WHITESPACECHANGES']._serialized_start=752
  _globals['_COMMITDIFFREQUEST_WHITESPACECHANGES']._serialized_end=873
  _globals['_COMMITDIFFRESPONSE']._serialized_start=908
  _globals['_COMMITDIFFRESPONSE']._serialized_end=1163
  _globals['_COMMITDELTAREQUEST']._serialized_start=1166
  _globals['_COMMITDELTAREQUEST']._serialized_end=1296
  _globals['_COMMITDELTA']._serialized_start=1298
  _globals['_COMMITDELTA']._serialized_end=1415
  _globals['_COMMITDELTARESPONSE']._serialized_start=1417
  _globals['_COMMITDELTARESPONSE']._serialized_end=1475
  _globals['_RAWDIFFREQUEST']._serialized_start=1477
  _globals['_RAWDIFFREQUEST']._serialized_end=1588
  _globals['_RAWDIFFRESPONSE']._serialized_start=1590
  _globals['_RAWDIFFRESPONSE']._serialized_end=1621
  _globals['_RAWPATCHREQUEST']._serialized_start=1623
  _globals['_RAWPATCHREQUEST']._serialized_end=1735
  _globals['_RAWPATCHRESPONSE']._serialized_start=1737
  _globals['_RAWPATCHRESPONSE']._serialized_end=1769
  _globals['_DIFFSTATSREQUEST']._serialized_start=1771
  _globals['_DIFFSTATSREQUEST']._serialized_end=1884
  _globals['_DIFFSTATS']._serialized_start=1886
  _globals['_DIFFSTATS']._serialized_end=1967
  _globals['_DIFFSTATSRESPONSE']._serialized_start=1969
  _globals['_DIFFSTATSRESPONSE']._serialized_end=2022
  _globals['_FINDCHANGEDPATHSREQUEST']._serialized_start=2025
  _globals['_FINDCHANGEDPATHSREQUEST']._serialized_end=2755
  _globals['_FINDCHANGEDPATHSREQUEST_REQUEST']._serialized_start=2286
  _globals['_FINDCHANGEDPATHSREQUEST_REQUEST']._serialized_end=2608
  _globals['_FINDCHANGEDPATHSREQUEST_REQUEST_TREEREQUEST']._serialized_start=2455
  _globals['_FINDCHANGEDPATHSREQUEST_REQUEST_TREEREQUEST']._serialized_end=2525
  _globals['_FINDCHANGEDPATHSREQUEST_REQUEST_COMMITREQUEST']._serialized_start=2527
  _globals['_FINDCHANGEDPATHSREQUEST_REQUEST_COMMITREQUEST']._serialized_end=2600
  _globals['_FINDCHANGEDPATHSREQUEST_MERGECOMMITDIFFMODE']._serialized_start=2611
  _globals['_FINDCHANGEDPATHSREQUEST_MERGECOMMITDIFFMODE']._serialized_end=2755
  _globals['_FINDCHANGEDPATHSRESPONSE']._serialized_start=2757
  _globals['_FINDCHANGEDPATHSRESPONSE']._serialized_end=2820
  _globals['_CHANGEDPATHS']._serialized_start=2823
  _globals['_CHANGEDPATHS']._serialized_end=3082
  _globals['_CHANGEDPATHS_STATUS']._serialized_start=2994
  _globals['_CHANGEDPATHS_STATUS']._serialized_end=3082
  _globals['_GETPATCHIDREQUEST']._serialized_start=3084
  _globals['_GETPATCHIDREQUEST']._serialized_end=3193
  _globals['_GETPATCHIDRESPONSE']._serialized_start=3195
  _globals['_GETPATCHIDRESPONSE']._serialized_end=3233
  _globals['_RANGEPAIR']._serialized_start=3235
  _globals['_RANGEPAIR']._serialized_end=3278
  _globals['_REVISIONRANGE']._serialized_start=3280
  _globals['_REVISIONRANGE']._serialized_end=3323
  _globals['_BASEWITHREVISIONS']._serialized_start=3325
  _globals['_BASEWITHREVISIONS']._serialized_end=3386
  _globals['_RAWRANGEDIFFREQUEST']._serialized_start=3389
  _globals['_RAWRANGEDIFFREQUEST']._serialized_end=3618
  _globals['_RAWRANGEDIFFRESPONSE']._serialized_start=3620
  _globals['_RAWRANGEDIFFRESPONSE']._serialized_end=3656
  _globals['_RANGEDIFFREQUEST']._serialized_start=3659
  _globals['_RANGEDIFFREQUEST']._serialized_end=3885
  _globals['_RANGEDIFFRESPONSE']._serialized_start=3888
  _globals['_RANGEDIFFRESPONSE']._serialized_end=4212
  _globals['_RANGEDIFFRESPONSE_COMPARATOR']._serialized_start=4085
  _globals['_RANGEDIFFRESPONSE_COMPARATOR']._serialized_end=4212
  _globals['_DIFFBLOBSREQUEST']._serialized_start=4215
  _globals['_DIFFBLOBSREQUEST']._serialized_end=4720
  _globals['_DIFFBLOBSREQUEST_BLOBPAIR']._serialized_start=4489
  _globals['_DIFFBLOBSREQUEST_BLOBPAIR']._serialized_end=4538
  _globals['_DIFFBLOBSREQUEST_DIFFMODE']._serialized_start=4540
  _globals['_DIFFBLOBSREQUEST_DIFFMODE']._serialized_end=4597
  _globals['_DIFFBLOBSREQUEST_WHITESPACECHANGES']._serialized_start=752
  _globals['_DIFFBLOBSREQUEST_WHITESPACECHANGES']._serialized_end=873
  _globals['_DIFFBLOBSRESPONSE']._serialized_start=4723
  _globals['_DIFFBLOBSRESPONSE']._serialized_end=4958
  _globals['_DIFFBLOBSRESPONSE_STATUS']._serialized_start=4902
  _globals['_DIFFBLOBSRESPONSE_STATUS']._serialized_end=4958
  _globals['_DIFFSERVICE']._serialized_start=4961
  _globals['_DIFFSERVICE']._serialized_end=5765
# @@protoc_insertion_point(module_scope)
