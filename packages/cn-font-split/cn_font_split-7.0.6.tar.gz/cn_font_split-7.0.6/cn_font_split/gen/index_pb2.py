# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: index.proto
# Protobuf Python Version: 5.28.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    3,
    '',
    'index.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bindex.proto\x12\rapi_interface\"\xcb\x0b\n\rInputTemplate\x12\r\n\x05input\x18\x01 \x01(\x0c\x12\x14\n\x07out_dir\x18\x02 \x01(\tH\x00\x88\x01\x01\x12<\n\x03\x63ss\x18\x05 \x01(\x0b\x32*.api_interface.InputTemplate.CssPropertiesH\x01\x88\x01\x01\x12\x18\n\x0btarget_type\x18\x06 \x01(\tH\x02\x88\x01\x01\x12\x0f\n\x07subsets\x18\x07 \x03(\x0c\x12\x17\n\nchunk_size\x18\t \x01(\x05H\x03\x88\x01\x01\x12!\n\x14\x63hunk_size_tolerance\x18\n \x01(\x02H\x04\x88\x01\x01\x12$\n\x17max_allow_subsets_count\x18\x0b \x01(\x05H\x05\x88\x01\x01\x12\x16\n\ttest_html\x18\r \x01(\x08H\x06\x88\x01\x01\x12\x15\n\x08reporter\x18\x0e \x01(\x08H\x07\x88\x01\x01\x12\x45\n\rpreview_image\x18\x0f \x01(\x0b\x32).api_interface.InputTemplate.PreviewImageH\x08\x88\x01\x01\x12\x1f\n\x12rename_output_font\x18\x12 \x01(\tH\t\x88\x01\x01\x12\x17\n\nbuild_mode\x18\x14 \x01(\tH\n\x88\x01\x01\x12\x1b\n\x0elanguage_areas\x18\x08 \x01(\x08H\x0b\x88\x01\x01\x12\x1a\n\rmulti_threads\x18\x15 \x01(\x08H\x0c\x88\x01\x01\x12\x19\n\x0c\x66ont_feature\x18\x16 \x01(\x08H\r\x88\x01\x01\x12\x18\n\x0breduce_mins\x18\x17 \x01(\x08H\x0e\x88\x01\x01\x12\x18\n\x0b\x61uto_subset\x18\x18 \x01(\x08H\x0f\x88\x01\x01\x12 \n\x13subset_remain_chars\x18\x19 \x01(\x08H\x10\x88\x01\x01\x1a\xec\x03\n\rCssProperties\x12\x18\n\x0b\x66ont_family\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x18\n\x0b\x66ont_weight\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x17\n\nfont_style\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x19\n\x0c\x66ont_display\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x14\n\x0clocal_family\x18\x05 \x03(\t\x12;\n\x08polyfill\x18\x06 \x03(\x0b\x32).api_interface.InputTemplate.PolyfillType\x12\x19\n\x0c\x63omment_base\x18\x0b \x01(\x08H\x04\x88\x01\x01\x12\x1f\n\x12\x63omment_name_table\x18\x0c \x01(\x08H\x05\x88\x01\x01\x12\x1d\n\x10\x63omment_unicodes\x18\r \x01(\x08H\x06\x88\x01\x01\x12\x15\n\x08\x63ompress\x18\x08 \x01(\x08H\x07\x88\x01\x01\x12\x16\n\tfile_name\x18\t \x01(\tH\x08\x88\x01\x01\x42\x0e\n\x0c_font_familyB\x0e\n\x0c_font_weightB\r\n\x0b_font_styleB\x0f\n\r_font_displayB\x0f\n\r_comment_baseB\x15\n\x13_comment_name_tableB\x13\n\x11_comment_unicodesB\x0b\n\t_compressB\x0c\n\n_file_name\x1a,\n\x0cPolyfillType\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06\x66ormat\x18\x02 \x01(\t\x1a*\n\x0cPreviewImage\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\tB\n\n\x08_out_dirB\x06\n\x04_cssB\x0e\n\x0c_target_typeB\r\n\x0b_chunk_sizeB\x17\n\x15_chunk_size_toleranceB\x1a\n\x18_max_allow_subsets_countB\x0c\n\n_test_htmlB\x0b\n\t_reporterB\x10\n\x0e_preview_imageB\x15\n\x13_rename_output_fontB\r\n\x0b_build_modeB\x11\n\x0f_language_areasB\x10\n\x0e_multi_threadsB\x0f\n\r_font_featureB\x0e\n\x0c_reduce_minsB\x0e\n\x0c_auto_subsetB\x16\n\x14_subset_remain_chars\"d\n\x0c\x45ventMessage\x12\'\n\x05\x65vent\x18\x01 \x01(\x0e\x32\x18.api_interface.EventName\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x11\n\x04\x64\x61ta\x18\x03 \x01(\x0cH\x00\x88\x01\x01\x42\x07\n\x05_data\">\n\rMultiMessages\x12-\n\x08messages\x18\x01 \x03(\x0b\x32\x1b.api_interface.EventMessage\"\xf6\x04\n\x0cOutputReport\x12\x0f\n\x07version\x18\x01 \x01(\t\x12,\n\x03\x63ss\x18\x02 \x01(\x0b\x32\x1f.api_interface.OutputReport.Css\x12\x10\n\x08platform\x18\x03 \x01(\t\x12\x41\n\x0e\x62undle_message\x18\x18 \x01(\x0b\x32).api_interface.OutputReport.BundleMessage\x12\x39\n\nname_table\x18\x19 \x03(\x0b\x32%.api_interface.OutputReport.NameTable\x12?\n\rsubset_detail\x18\x1a \x03(\x0b\x32(.api_interface.OutputReport.SubsetDetail\x1aL\n\tNameTable\x12\x10\n\x08platform\x18\x01 \x01(\t\x12\x10\n\x08language\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\r\n\x05value\x18\x04 \x01(\t\x1aX\n\x0cSubsetDetail\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04hash\x18\x02 \x01(\t\x12\r\n\x05\x62ytes\x18\x03 \x01(\r\x12\r\n\x05\x63hars\x18\x04 \x03(\r\x12\x10\n\x08\x64uration\x18\x05 \x01(\r\x1ag\n\rBundleMessage\x12\x13\n\x0borigin_size\x18\x01 \x01(\r\x12\x14\n\x0c\x62undled_size\x18\x02 \x01(\r\x12\x14\n\x0corigin_bytes\x18\x03 \x01(\r\x12\x15\n\rbundled_bytes\x18\x04 \x01(\r\x1a\x45\n\x03\x43ss\x12\x0e\n\x06\x66\x61mily\x18\x01 \x01(\t\x12\r\n\x05style\x18\x02 \x01(\t\x12\x0e\n\x06weight\x18\x03 \x01(\t\x12\x0f\n\x07\x64isplay\x18\x04 \x01(\t*6\n\tEventName\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0f\n\x0bOUTPUT_DATA\x10\x01\x12\x07\n\x03\x45ND\x10\x02\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'index_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EVENTNAME']._serialized_start=2315
  _globals['_EVENTNAME']._serialized_end=2369
  _globals['_INPUTTEMPLATE']._serialized_start=31
  _globals['_INPUTTEMPLATE']._serialized_end=1514
  _globals['_INPUTTEMPLATE_CSSPROPERTIES']._serialized_start=635
  _globals['_INPUTTEMPLATE_CSSPROPERTIES']._serialized_end=1127
  _globals['_INPUTTEMPLATE_POLYFILLTYPE']._serialized_start=1129
  _globals['_INPUTTEMPLATE_POLYFILLTYPE']._serialized_end=1173
  _globals['_INPUTTEMPLATE_PREVIEWIMAGE']._serialized_start=1175
  _globals['_INPUTTEMPLATE_PREVIEWIMAGE']._serialized_end=1217
  _globals['_EVENTMESSAGE']._serialized_start=1516
  _globals['_EVENTMESSAGE']._serialized_end=1616
  _globals['_MULTIMESSAGES']._serialized_start=1618
  _globals['_MULTIMESSAGES']._serialized_end=1680
  _globals['_OUTPUTREPORT']._serialized_start=1683
  _globals['_OUTPUTREPORT']._serialized_end=2313
  _globals['_OUTPUTREPORT_NAMETABLE']._serialized_start=1971
  _globals['_OUTPUTREPORT_NAMETABLE']._serialized_end=2047
  _globals['_OUTPUTREPORT_SUBSETDETAIL']._serialized_start=2049
  _globals['_OUTPUTREPORT_SUBSETDETAIL']._serialized_end=2137
  _globals['_OUTPUTREPORT_BUNDLEMESSAGE']._serialized_start=2139
  _globals['_OUTPUTREPORT_BUNDLEMESSAGE']._serialized_end=2242
  _globals['_OUTPUTREPORT_CSS']._serialized_start=2244
  _globals['_OUTPUTREPORT_CSS']._serialized_end=2313
# @@protoc_insertion_point(module_scope)
