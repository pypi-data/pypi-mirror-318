"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 28, 1, '', 'google/example/library/v1/library.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'google/example/library/v1/library.proto\x12\x19google.example.library.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\x89\x01\n\x04Book\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06author\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12\x0c\n\x04read\x18\x04 \x01(\x08:F\xeaAC\n#library-example.googleapis.com/Book\x12\x1cshelves/{shelf}/books/{book}"c\n\x05Shelf\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05theme\x18\x02 \x01(\t:=\xeaA:\n$library-example.googleapis.com/Shelf\x12\x12shelves/{shelf_id}"J\n\x12CreateShelfRequest\x124\n\x05shelf\x18\x01 \x01(\x0b2 .google.example.library.v1.ShelfB\x03\xe0A\x02"M\n\x0fGetShelfRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$library-example.googleapis.com/Shelf";\n\x12ListShelvesRequest\x12\x11\n\tpage_size\x18\x01 \x01(\x05\x12\x12\n\npage_token\x18\x02 \x01(\t"a\n\x13ListShelvesResponse\x121\n\x07shelves\x18\x01 \x03(\x0b2 .google.example.library.v1.Shelf\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"P\n\x12DeleteShelfRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$library-example.googleapis.com/Shelf"\x94\x01\n\x13MergeShelvesRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$library-example.googleapis.com/Shelf\x12A\n\x0bother_shelf\x18\x02 \x01(\tB,\xe0A\x02\xfaA&\n$library-example.googleapis.com/Shelf"\x85\x01\n\x11CreateBookRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$library-example.googleapis.com/Shelf\x122\n\x04book\x18\x02 \x01(\x0b2\x1f.google.example.library.v1.BookB\x03\xe0A\x02"K\n\x0eGetBookRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#library-example.googleapis.com/Book"w\n\x10ListBooksRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$library-example.googleapis.com/Shelf\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\\\n\x11ListBooksResponse\x12.\n\x05books\x18\x01 \x03(\x0b2\x1f.google.example.library.v1.Book\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"}\n\x11UpdateBookRequest\x122\n\x04book\x18\x01 \x01(\x0b2\x1f.google.example.library.v1.BookB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"N\n\x11DeleteBookRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#library-example.googleapis.com/Book"\x94\x01\n\x0fMoveBookRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#library-example.googleapis.com/Book\x12F\n\x10other_shelf_name\x18\x02 \x01(\tB,\xe0A\x02\xfaA&\n$library-example.googleapis.com/Shelf2\xcb\x0c\n\x0eLibraryService\x12\x82\x01\n\x0bCreateShelf\x12-.google.example.library.v1.CreateShelfRequest\x1a .google.example.library.v1.Shelf""\xdaA\x05shelf\x82\xd3\xe4\x93\x02\x14"\x0b/v1/shelves:\x05shelf\x12}\n\x08GetShelf\x12*.google.example.library.v1.GetShelfRequest\x1a .google.example.library.v1.Shelf"#\xdaA\x04name\x82\xd3\xe4\x93\x02\x16\x12\x14/v1/{name=shelves/*}\x12\x81\x01\n\x0bListShelves\x12-.google.example.library.v1.ListShelvesRequest\x1a..google.example.library.v1.ListShelvesResponse"\x13\x82\xd3\xe4\x93\x02\r\x12\x0b/v1/shelves\x12y\n\x0bDeleteShelf\x12-.google.example.library.v1.DeleteShelfRequest\x1a\x16.google.protobuf.Empty"#\xdaA\x04name\x82\xd3\xe4\x93\x02\x16*\x14/v1/{name=shelves/*}\x12\x9a\x01\n\x0cMergeShelves\x12..google.example.library.v1.MergeShelvesRequest\x1a .google.example.library.v1.Shelf"8\xdaA\x10name,other_shelf\x82\xd3\xe4\x93\x02\x1f"\x1a/v1/{name=shelves/*}:merge:\x01*\x12\x95\x01\n\nCreateBook\x12,.google.example.library.v1.CreateBookRequest\x1a\x1f.google.example.library.v1.Book"8\xdaA\x0bparent,book\x82\xd3\xe4\x93\x02$"\x1c/v1/{parent=shelves/*}/books:\x04book\x12\x82\x01\n\x07GetBook\x12).google.example.library.v1.GetBookRequest\x1a\x1f.google.example.library.v1.Book"+\xdaA\x04name\x82\xd3\xe4\x93\x02\x1e\x12\x1c/v1/{name=shelves/*/books/*}\x12\x95\x01\n\tListBooks\x12+.google.example.library.v1.ListBooksRequest\x1a,.google.example.library.v1.ListBooksResponse"-\xdaA\x06parent\x82\xd3\xe4\x93\x02\x1e\x12\x1c/v1/{parent=shelves/*}/books\x12\x7f\n\nDeleteBook\x12,.google.example.library.v1.DeleteBookRequest\x1a\x16.google.protobuf.Empty"+\xdaA\x04name\x82\xd3\xe4\x93\x02\x1e*\x1c/v1/{name=shelves/*/books/*}\x12\x9f\x01\n\nUpdateBook\x12,.google.example.library.v1.UpdateBookRequest\x1a\x1f.google.example.library.v1.Book"B\xdaA\x10book,update_mask\x82\xd3\xe4\x93\x02)2!/v1/{book.name=shelves/*/books/*}:\x04book\x12\x9d\x01\n\x08MoveBook\x12*.google.example.library.v1.MoveBookRequest\x1a\x1f.google.example.library.v1.Book"D\xdaA\x15name,other_shelf_name\x82\xd3\xe4\x93\x02&"!/v1/{name=shelves/*/books/*}:move:\x01*\x1a!\xcaA\x1elibrary-example.googleapis.comB\x93\x01\n\x1dcom.google.example.library.v1B\x0cLibraryProtoP\x01Z@google.golang.org/genproto/googleapis/example/library/v1;library\xca\x02\x1fGoogle\\Cloud\\Example\\Library\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.example.library.v1.library_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.example.library.v1B\x0cLibraryProtoP\x01Z@google.golang.org/genproto/googleapis/example/library/v1;library\xca\x02\x1fGoogle\\Cloud\\Example\\Library\\V1'
    _globals['_BOOK']._loaded_options = None
    _globals['_BOOK']._serialized_options = b'\xeaAC\n#library-example.googleapis.com/Book\x12\x1cshelves/{shelf}/books/{book}'
    _globals['_SHELF']._loaded_options = None
    _globals['_SHELF']._serialized_options = b'\xeaA:\n$library-example.googleapis.com/Shelf\x12\x12shelves/{shelf_id}'
    _globals['_CREATESHELFREQUEST'].fields_by_name['shelf']._loaded_options = None
    _globals['_CREATESHELFREQUEST'].fields_by_name['shelf']._serialized_options = b'\xe0A\x02'
    _globals['_GETSHELFREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSHELFREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$library-example.googleapis.com/Shelf'
    _globals['_DELETESHELFREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETESHELFREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$library-example.googleapis.com/Shelf'
    _globals['_MERGESHELVESREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_MERGESHELVESREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$library-example.googleapis.com/Shelf'
    _globals['_MERGESHELVESREQUEST'].fields_by_name['other_shelf']._loaded_options = None
    _globals['_MERGESHELVESREQUEST'].fields_by_name['other_shelf']._serialized_options = b'\xe0A\x02\xfaA&\n$library-example.googleapis.com/Shelf'
    _globals['_CREATEBOOKREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEBOOKREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA&\n$library-example.googleapis.com/Shelf'
    _globals['_CREATEBOOKREQUEST'].fields_by_name['book']._loaded_options = None
    _globals['_CREATEBOOKREQUEST'].fields_by_name['book']._serialized_options = b'\xe0A\x02'
    _globals['_GETBOOKREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETBOOKREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#library-example.googleapis.com/Book'
    _globals['_LISTBOOKSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTBOOKSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA&\n$library-example.googleapis.com/Shelf'
    _globals['_UPDATEBOOKREQUEST'].fields_by_name['book']._loaded_options = None
    _globals['_UPDATEBOOKREQUEST'].fields_by_name['book']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEBOOKREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEBOOKREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEBOOKREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEBOOKREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#library-example.googleapis.com/Book'
    _globals['_MOVEBOOKREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_MOVEBOOKREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#library-example.googleapis.com/Book'
    _globals['_MOVEBOOKREQUEST'].fields_by_name['other_shelf_name']._loaded_options = None
    _globals['_MOVEBOOKREQUEST'].fields_by_name['other_shelf_name']._serialized_options = b'\xe0A\x02\xfaA&\n$library-example.googleapis.com/Shelf'
    _globals['_LIBRARYSERVICE']._loaded_options = None
    _globals['_LIBRARYSERVICE']._serialized_options = b'\xcaA\x1elibrary-example.googleapis.com'
    _globals['_LIBRARYSERVICE'].methods_by_name['CreateShelf']._loaded_options = None
    _globals['_LIBRARYSERVICE'].methods_by_name['CreateShelf']._serialized_options = b'\xdaA\x05shelf\x82\xd3\xe4\x93\x02\x14"\x0b/v1/shelves:\x05shelf'
    _globals['_LIBRARYSERVICE'].methods_by_name['GetShelf']._loaded_options = None
    _globals['_LIBRARYSERVICE'].methods_by_name['GetShelf']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x16\x12\x14/v1/{name=shelves/*}'
    _globals['_LIBRARYSERVICE'].methods_by_name['ListShelves']._loaded_options = None
    _globals['_LIBRARYSERVICE'].methods_by_name['ListShelves']._serialized_options = b'\x82\xd3\xe4\x93\x02\r\x12\x0b/v1/shelves'
    _globals['_LIBRARYSERVICE'].methods_by_name['DeleteShelf']._loaded_options = None
    _globals['_LIBRARYSERVICE'].methods_by_name['DeleteShelf']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x16*\x14/v1/{name=shelves/*}'
    _globals['_LIBRARYSERVICE'].methods_by_name['MergeShelves']._loaded_options = None
    _globals['_LIBRARYSERVICE'].methods_by_name['MergeShelves']._serialized_options = b'\xdaA\x10name,other_shelf\x82\xd3\xe4\x93\x02\x1f"\x1a/v1/{name=shelves/*}:merge:\x01*'
    _globals['_LIBRARYSERVICE'].methods_by_name['CreateBook']._loaded_options = None
    _globals['_LIBRARYSERVICE'].methods_by_name['CreateBook']._serialized_options = b'\xdaA\x0bparent,book\x82\xd3\xe4\x93\x02$"\x1c/v1/{parent=shelves/*}/books:\x04book'
    _globals['_LIBRARYSERVICE'].methods_by_name['GetBook']._loaded_options = None
    _globals['_LIBRARYSERVICE'].methods_by_name['GetBook']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x1e\x12\x1c/v1/{name=shelves/*/books/*}'
    _globals['_LIBRARYSERVICE'].methods_by_name['ListBooks']._loaded_options = None
    _globals['_LIBRARYSERVICE'].methods_by_name['ListBooks']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\x1e\x12\x1c/v1/{parent=shelves/*}/books'
    _globals['_LIBRARYSERVICE'].methods_by_name['DeleteBook']._loaded_options = None
    _globals['_LIBRARYSERVICE'].methods_by_name['DeleteBook']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x1e*\x1c/v1/{name=shelves/*/books/*}'
    _globals['_LIBRARYSERVICE'].methods_by_name['UpdateBook']._loaded_options = None
    _globals['_LIBRARYSERVICE'].methods_by_name['UpdateBook']._serialized_options = b'\xdaA\x10book,update_mask\x82\xd3\xe4\x93\x02)2!/v1/{book.name=shelves/*/books/*}:\x04book'
    _globals['_LIBRARYSERVICE'].methods_by_name['MoveBook']._loaded_options = None
    _globals['_LIBRARYSERVICE'].methods_by_name['MoveBook']._serialized_options = b'\xdaA\x15name,other_shelf_name\x82\xd3\xe4\x93\x02&"!/v1/{name=shelves/*/books/*}:move:\x01*'
    _globals['_BOOK']._serialized_start = 249
    _globals['_BOOK']._serialized_end = 386
    _globals['_SHELF']._serialized_start = 388
    _globals['_SHELF']._serialized_end = 487
    _globals['_CREATESHELFREQUEST']._serialized_start = 489
    _globals['_CREATESHELFREQUEST']._serialized_end = 563
    _globals['_GETSHELFREQUEST']._serialized_start = 565
    _globals['_GETSHELFREQUEST']._serialized_end = 642
    _globals['_LISTSHELVESREQUEST']._serialized_start = 644
    _globals['_LISTSHELVESREQUEST']._serialized_end = 703
    _globals['_LISTSHELVESRESPONSE']._serialized_start = 705
    _globals['_LISTSHELVESRESPONSE']._serialized_end = 802
    _globals['_DELETESHELFREQUEST']._serialized_start = 804
    _globals['_DELETESHELFREQUEST']._serialized_end = 884
    _globals['_MERGESHELVESREQUEST']._serialized_start = 887
    _globals['_MERGESHELVESREQUEST']._serialized_end = 1035
    _globals['_CREATEBOOKREQUEST']._serialized_start = 1038
    _globals['_CREATEBOOKREQUEST']._serialized_end = 1171
    _globals['_GETBOOKREQUEST']._serialized_start = 1173
    _globals['_GETBOOKREQUEST']._serialized_end = 1248
    _globals['_LISTBOOKSREQUEST']._serialized_start = 1250
    _globals['_LISTBOOKSREQUEST']._serialized_end = 1369
    _globals['_LISTBOOKSRESPONSE']._serialized_start = 1371
    _globals['_LISTBOOKSRESPONSE']._serialized_end = 1463
    _globals['_UPDATEBOOKREQUEST']._serialized_start = 1465
    _globals['_UPDATEBOOKREQUEST']._serialized_end = 1590
    _globals['_DELETEBOOKREQUEST']._serialized_start = 1592
    _globals['_DELETEBOOKREQUEST']._serialized_end = 1670
    _globals['_MOVEBOOKREQUEST']._serialized_start = 1673
    _globals['_MOVEBOOKREQUEST']._serialized_end = 1821
    _globals['_LIBRARYSERVICE']._serialized_start = 1824
    _globals['_LIBRARYSERVICE']._serialized_end = 3435