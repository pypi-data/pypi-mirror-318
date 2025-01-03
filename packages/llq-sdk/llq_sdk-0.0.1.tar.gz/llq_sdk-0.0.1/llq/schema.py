import sgqlc.types
import sgqlc.types.relay


schema = sgqlc.types.Schema()


# Unexport Node/PageInfo, let schema re-declare them
schema -= sgqlc.types.relay.Node
schema -= sgqlc.types.relay.PageInfo



########################################################################
# Scalars and Enumerations
########################################################################
class AvatarRatingEnum(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('G', 'PG', 'R', 'X')


Boolean = sgqlc.types.Boolean

class CategoryIdType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DATABASE_ID', 'ID', 'NAME', 'SLUG', 'URI')


class CommentNodeIdTypeEnum(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DATABASE_ID', 'ID')


class CommentStatusEnum(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('APPROVE', 'HOLD', 'SPAM', 'TRASH')


class CommentsConnectionOrderbyEnum(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('COMMENT_AGENT', 'COMMENT_APPROVED', 'COMMENT_AUTHOR', 'COMMENT_AUTHOR_EMAIL', 'COMMENT_AUTHOR_IP', 'COMMENT_AUTHOR_URL', 'COMMENT_CONTENT', 'COMMENT_DATE', 'COMMENT_DATE_GMT', 'COMMENT_ID', 'COMMENT_IN', 'COMMENT_KARMA', 'COMMENT_PARENT', 'COMMENT_POST_ID', 'COMMENT_TYPE', 'USER_ID')


class ContentNodeIdTypeEnum(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DATABASE_ID', 'ID', 'URI')


class ContentTypeEnum(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ATTACHMENT', 'GRAPHQL_DOCUMENT', 'JOB', 'PAGE', 'PARTNER', 'POST', 'TRIBE_EVENTS', 'TRIBE_ORGANIZER', 'TRIBE_VENUE')


class ContentTypeIdTypeEnum(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ID', 'NAME')


class ContentTypesOfCategoryEnum(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('POST',)


class ContentTypesOfContractKindEnum(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('JOB',)


class ContentTypesOfEventsCategoryEnum(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('TRIBE_EVENTS',)


class ContentTypesOfGraphqlDocumentGroupEnum(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('GRAPHQL_DOCUMENT',)


class ContentTypesOfJobmodeEnum(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('JOB',)


class ContentTypesOfOccupationkindEnum(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('JOB',)


class ContentTypesOfPostFormatEnum(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('POST',)


class ContentTypesOfTagEnum(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('POST', 'TRIBE_EVENTS')


class ContractKindIdType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DATABASE_ID', 'ID', 'NAME', 'SLUG', 'URI')


class EventIdType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DATABASE_ID', 'ID', 'SLUG', 'URI')


class EventsCategoryIdType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DATABASE_ID', 'ID', 'NAME', 'SLUG', 'URI')


Float = sgqlc.types.Float

class GraphqlDocumentGroupIdType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DATABASE_ID', 'ID', 'NAME', 'SLUG', 'URI')


class GraphqlDocumentIdType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DATABASE_ID', 'ID', 'SLUG', 'URI')


ID = sgqlc.types.ID

Int = sgqlc.types.Int

class JobIdType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DATABASE_ID', 'ID', 'SLUG', 'URI')


class JobmodeIdType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DATABASE_ID', 'ID', 'NAME', 'SLUG', 'URI')


class MediaItemIdType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DATABASE_ID', 'ID', 'SLUG', 'SOURCE_URL', 'URI')


class MediaItemSizeEnum(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('LARGE', 'MEDIUM', 'MEDIUM_LARGE', 'THUMBNAIL', '_1536X1536', '_2048X2048')


class MediaItemStatusEnum(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('AUTO_DRAFT', 'INHERIT', 'PRIVATE', 'TRASH')


class MenuItemNodeIdTypeEnum(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DATABASE_ID', 'ID')


class MenuLocationEnum(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('EMPTY',)


class MenuNodeIdTypeEnum(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DATABASE_ID', 'ID', 'LOCATION', 'NAME', 'SLUG')


class MimeTypeEnum(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('APPLICATION_JAVA', 'APPLICATION_MSWORD', 'APPLICATION_OCTET_STREAM', 'APPLICATION_ONENOTE', 'APPLICATION_OXPS', 'APPLICATION_PDF', 'APPLICATION_RAR', 'APPLICATION_RTF', 'APPLICATION_TTAF_XML', 'APPLICATION_VND_APPLE_KEYNOTE', 'APPLICATION_VND_APPLE_NUMBERS', 'APPLICATION_VND_APPLE_PAGES', 'APPLICATION_VND_MS_ACCESS', 'APPLICATION_VND_MS_EXCEL', 'APPLICATION_VND_MS_EXCEL_ADDIN_MACROENABLED_12', 'APPLICATION_VND_MS_EXCEL_SHEET_BINARY_MACROENABLED_12', 'APPLICATION_VND_MS_EXCEL_SHEET_MACROENABLED_12', 'APPLICATION_VND_MS_EXCEL_TEMPLATE_MACROENABLED_12', 'APPLICATION_VND_MS_POWERPOINT', 'APPLICATION_VND_MS_POWERPOINT_ADDIN_MACROENABLED_12', 'APPLICATION_VND_MS_POWERPOINT_PRESENTATION_MACROENABLED_12', 'APPLICATION_VND_MS_POWERPOINT_SLIDESHOW_MACROENABLED_12', 'APPLICATION_VND_MS_POWERPOINT_SLIDE_MACROENABLED_12', 'APPLICATION_VND_MS_POWERPOINT_TEMPLATE_MACROENABLED_12', 'APPLICATION_VND_MS_PROJECT', 'APPLICATION_VND_MS_WORD_DOCUMENT_MACROENABLED_12', 'APPLICATION_VND_MS_WORD_TEMPLATE_MACROENABLED_12', 'APPLICATION_VND_MS_WRITE', 'APPLICATION_VND_MS_XPSDOCUMENT', 'APPLICATION_VND_OASIS_OPENDOCUMENT_CHART', 'APPLICATION_VND_OASIS_OPENDOCUMENT_DATABASE', 'APPLICATION_VND_OASIS_OPENDOCUMENT_FORMULA', 'APPLICATION_VND_OASIS_OPENDOCUMENT_GRAPHICS', 'APPLICATION_VND_OASIS_OPENDOCUMENT_PRESENTATION', 'APPLICATION_VND_OASIS_OPENDOCUMENT_SPREADSHEET', 'APPLICATION_VND_OASIS_OPENDOCUMENT_TEXT', 'APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_PRESENTATIONML_PRESENTATION', 'APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_PRESENTATIONML_SLIDE', 'APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_PRESENTATIONML_SLIDESHOW', 'APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_PRESENTATIONML_TEMPLATE', 'APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_SPREADSHEETML_SHEET', 'APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_SPREADSHEETML_TEMPLATE', 'APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_WORDPROCESSINGML_DOCUMENT', 'APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_WORDPROCESSINGML_TEMPLATE', 'APPLICATION_WORDPERFECT', 'APPLICATION_X_7Z_COMPRESSED', 'APPLICATION_X_GZIP', 'APPLICATION_X_TAR', 'APPLICATION_ZIP', 'AUDIO_AAC', 'AUDIO_FLAC', 'AUDIO_MIDI', 'AUDIO_MPEG', 'AUDIO_OGG', 'AUDIO_WAV', 'AUDIO_X_MATROSKA', 'AUDIO_X_MS_WAX', 'AUDIO_X_MS_WMA', 'AUDIO_X_REALAUDIO', 'IMAGE_AVIF', 'IMAGE_BMP', 'IMAGE_GIF', 'IMAGE_HEIC', 'IMAGE_HEIC_SEQUENCE', 'IMAGE_HEIF', 'IMAGE_HEIF_SEQUENCE', 'IMAGE_JPEG', 'IMAGE_PNG', 'IMAGE_TIFF', 'IMAGE_WEBP', 'IMAGE_X_ICON', 'TEXT_CALENDAR', 'TEXT_CSS', 'TEXT_CSV', 'TEXT_PLAIN', 'TEXT_RICHTEXT', 'TEXT_TAB_SEPARATED_VALUES', 'TEXT_VTT', 'VIDEO_3GPP', 'VIDEO_3GPP2', 'VIDEO_AVI', 'VIDEO_DIVX', 'VIDEO_MP4', 'VIDEO_MPEG', 'VIDEO_OGG', 'VIDEO_QUICKTIME', 'VIDEO_WEBM', 'VIDEO_X_FLV', 'VIDEO_X_MATROSKA', 'VIDEO_X_MS_ASF', 'VIDEO_X_MS_WM', 'VIDEO_X_MS_WMV', 'VIDEO_X_MS_WMX')


class OccupationkindIdType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DATABASE_ID', 'ID', 'NAME', 'SLUG', 'URI')


class OrderEnum(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ASC', 'DESC')


class OrganizerIdType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DATABASE_ID', 'ID', 'SLUG', 'URI')


class PageIdType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DATABASE_ID', 'ID', 'URI')


class PartnerIdType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DATABASE_ID', 'ID', 'SLUG', 'URI')


class PluginStatusEnum(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ACTIVE', 'DROP_IN', 'INACTIVE', 'MUST_USE', 'PAUSED', 'RECENTLY_ACTIVE', 'UPGRADE')


class PostFormatIdType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DATABASE_ID', 'ID', 'NAME', 'SLUG', 'URI')


class PostIdType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DATABASE_ID', 'ID', 'SLUG', 'URI')


class PostObjectFieldFormatEnum(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('RAW', 'RENDERED')


class PostObjectsConnectionDateColumnEnum(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DATE', 'MODIFIED')


class PostObjectsConnectionOrderbyEnum(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('AUTHOR', 'COMMENT_COUNT', 'DATE', 'IN', 'MENU_ORDER', 'MODIFIED', 'NAME_IN', 'PARENT', 'SLUG', 'TITLE')


class PostStatusEnum(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ACF_DISABLED', 'AUTO_DRAFT', 'DRAFT', 'FUTURE', 'INHERIT', 'PENDING', 'PRIVATE', 'PUBLISH', 'REQUEST_COMPLETED', 'REQUEST_CONFIRMED', 'REQUEST_FAILED', 'REQUEST_PENDING', 'TRASH', 'TRIBE_EA_DRAFT', 'TRIBE_EA_FAILED', 'TRIBE_EA_PENDING', 'TRIBE_EA_SCHEDULE', 'TRIBE_EA_SUCCESS', 'TRIBE_IGNORED')


class RelationEnum(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('AND', 'OR')


class ScriptLoadingStrategyEnum(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ASYNC', 'DEFER')


String = sgqlc.types.String

class TagIdType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DATABASE_ID', 'ID', 'NAME', 'SLUG', 'URI')


class TaxonomyEnum(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CATEGORY', 'CONTRACTKIND', 'EVENTSCATEGORY', 'GRAPHQLDOCUMENTGROUP', 'JOBMODE', 'OCCUPATIONKIND', 'POSTFORMAT', 'TAG')


class TaxonomyIdTypeEnum(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ID', 'NAME')


class TermNodeIdTypeEnum(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DATABASE_ID', 'ID', 'NAME', 'SLUG', 'URI')


class TermObjectsConnectionOrderbyEnum(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('COUNT', 'DESCRIPTION', 'NAME', 'SLUG', 'TERM_GROUP', 'TERM_ID', 'TERM_ORDER')


class UserNodeIdTypeEnum(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DATABASE_ID', 'EMAIL', 'ID', 'SLUG', 'URI', 'USERNAME')


class UserRoleEnum(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ADMINISTRATOR', 'AUTHOR', 'CONTRIBUTOR', 'EDITOR', 'SEO_EDITOR', 'SEO_MANAGER', 'SUBSCRIBER')


class UsersConnectionOrderbyEnum(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DISPLAY_NAME', 'EMAIL', 'LOGIN', 'LOGIN_IN', 'NICE_NAME', 'NICE_NAME_IN', 'REGISTERED', 'URL')


class UsersConnectionSearchColumnEnum(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('EMAIL', 'ID', 'LOGIN', 'NICENAME', 'URL')


class VenueIdType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DATABASE_ID', 'ID', 'SLUG', 'URI')



########################################################################
# Input Objects
########################################################################
class CategoryToCategoryConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('cache_domain', 'child_of', 'childless', 'description_like', 'exclude', 'exclude_tree', 'hide_empty', 'hierarchical', 'include', 'name', 'name_like', 'object_ids', 'order', 'orderby', 'pad_counts', 'parent', 'search', 'slug', 'term_taxonom_id', 'term_taxonomy_id', 'update_term_meta_cache')
    cache_domain = sgqlc.types.Field(String, graphql_name='cacheDomain')
    child_of = sgqlc.types.Field(Int, graphql_name='childOf')
    childless = sgqlc.types.Field(Boolean, graphql_name='childless')
    description_like = sgqlc.types.Field(String, graphql_name='descriptionLike')
    exclude = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='exclude')
    exclude_tree = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='excludeTree')
    hide_empty = sgqlc.types.Field(Boolean, graphql_name='hideEmpty')
    hierarchical = sgqlc.types.Field(Boolean, graphql_name='hierarchical')
    include = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='include')
    name = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='name')
    name_like = sgqlc.types.Field(String, graphql_name='nameLike')
    object_ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='objectIds')
    order = sgqlc.types.Field(OrderEnum, graphql_name='order')
    orderby = sgqlc.types.Field(TermObjectsConnectionOrderbyEnum, graphql_name='orderby')
    pad_counts = sgqlc.types.Field(Boolean, graphql_name='padCounts')
    parent = sgqlc.types.Field(Int, graphql_name='parent')
    search = sgqlc.types.Field(String, graphql_name='search')
    slug = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='slug')
    term_taxonom_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomId')
    term_taxonomy_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomyId')
    update_term_meta_cache = sgqlc.types.Field(Boolean, graphql_name='updateTermMetaCache')


class CategoryToContentNodeConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('content_types', 'date_query', 'has_password', 'id', 'in_', 'mime_type', 'name', 'name_in', 'not_in', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'password', 'search', 'stati', 'status', 'title')
    content_types = sgqlc.types.Field(sgqlc.types.list_of(ContentTypesOfCategoryEnum), graphql_name='contentTypes')
    date_query = sgqlc.types.Field('DateQueryInput', graphql_name='dateQuery')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    id = sgqlc.types.Field(Int, graphql_name='id')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')
    mime_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='mimeType')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nameIn')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='notIn')
    orderby = sgqlc.types.Field(sgqlc.types.list_of('PostObjectsConnectionOrderbyInput'), graphql_name='orderby')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    password = sgqlc.types.Field(String, graphql_name='password')
    search = sgqlc.types.Field(String, graphql_name='search')
    stati = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='stati')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class CategoryToPostConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author', 'author_in', 'author_name', 'author_not_in', 'category_id', 'category_in', 'category_name', 'category_not_in', 'date_query', 'has_password', 'id', 'in_', 'mime_type', 'name', 'name_in', 'not_in', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'password', 'search', 'stati', 'status', 'tag', 'tag_id', 'tag_in', 'tag_not_in', 'tag_slug_and', 'tag_slug_in', 'title')
    author = sgqlc.types.Field(Int, graphql_name='author')
    author_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorIn')
    author_name = sgqlc.types.Field(String, graphql_name='authorName')
    author_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorNotIn')
    category_id = sgqlc.types.Field(Int, graphql_name='categoryId')
    category_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='categoryIn')
    category_name = sgqlc.types.Field(String, graphql_name='categoryName')
    category_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='categoryNotIn')
    date_query = sgqlc.types.Field('DateQueryInput', graphql_name='dateQuery')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    id = sgqlc.types.Field(Int, graphql_name='id')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')
    mime_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='mimeType')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nameIn')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='notIn')
    orderby = sgqlc.types.Field(sgqlc.types.list_of('PostObjectsConnectionOrderbyInput'), graphql_name='orderby')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    password = sgqlc.types.Field(String, graphql_name='password')
    search = sgqlc.types.Field(String, graphql_name='search')
    stati = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='stati')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    tag = sgqlc.types.Field(String, graphql_name='tag')
    tag_id = sgqlc.types.Field(String, graphql_name='tagId')
    tag_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='tagIn')
    tag_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='tagNotIn')
    tag_slug_and = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tagSlugAnd')
    tag_slug_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tagSlugIn')
    title = sgqlc.types.Field(String, graphql_name='title')


class CommentToCommentConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author_email', 'author_in', 'author_not_in', 'author_url', 'comment_in', 'comment_not_in', 'comment_type', 'comment_type_in', 'comment_type_not_in', 'content_author', 'content_author_in', 'content_author_not_in', 'content_id', 'content_id_in', 'content_id_not_in', 'content_name', 'content_parent', 'content_status', 'content_type', 'include_unapproved', 'karma', 'order', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'search', 'status', 'user_id')
    author_email = sgqlc.types.Field(String, graphql_name='authorEmail')
    author_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorIn')
    author_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorNotIn')
    author_url = sgqlc.types.Field(String, graphql_name='authorUrl')
    comment_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='commentIn')
    comment_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='commentNotIn')
    comment_type = sgqlc.types.Field(String, graphql_name='commentType')
    comment_type_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='commentTypeIn')
    comment_type_not_in = sgqlc.types.Field(String, graphql_name='commentTypeNotIn')
    content_author = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='contentAuthor')
    content_author_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='contentAuthorIn')
    content_author_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='contentAuthorNotIn')
    content_id = sgqlc.types.Field(ID, graphql_name='contentId')
    content_id_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='contentIdIn')
    content_id_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='contentIdNotIn')
    content_name = sgqlc.types.Field(String, graphql_name='contentName')
    content_parent = sgqlc.types.Field(Int, graphql_name='contentParent')
    content_status = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='contentStatus')
    content_type = sgqlc.types.Field(sgqlc.types.list_of(ContentTypeEnum), graphql_name='contentType')
    include_unapproved = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='includeUnapproved')
    karma = sgqlc.types.Field(Int, graphql_name='karma')
    order = sgqlc.types.Field(OrderEnum, graphql_name='order')
    orderby = sgqlc.types.Field(CommentsConnectionOrderbyEnum, graphql_name='orderby')
    parent = sgqlc.types.Field(Int, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    search = sgqlc.types.Field(String, graphql_name='search')
    status = sgqlc.types.Field(String, graphql_name='status')
    user_id = sgqlc.types.Field(ID, graphql_name='userId')


class CommentToParentCommentConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author_email', 'author_in', 'author_not_in', 'author_url', 'comment_in', 'comment_not_in', 'comment_type', 'comment_type_in', 'comment_type_not_in', 'content_author', 'content_author_in', 'content_author_not_in', 'content_id', 'content_id_in', 'content_id_not_in', 'content_name', 'content_parent', 'content_status', 'content_type', 'include_unapproved', 'karma', 'order', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'search', 'status', 'user_id')
    author_email = sgqlc.types.Field(String, graphql_name='authorEmail')
    author_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorIn')
    author_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorNotIn')
    author_url = sgqlc.types.Field(String, graphql_name='authorUrl')
    comment_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='commentIn')
    comment_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='commentNotIn')
    comment_type = sgqlc.types.Field(String, graphql_name='commentType')
    comment_type_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='commentTypeIn')
    comment_type_not_in = sgqlc.types.Field(String, graphql_name='commentTypeNotIn')
    content_author = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='contentAuthor')
    content_author_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='contentAuthorIn')
    content_author_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='contentAuthorNotIn')
    content_id = sgqlc.types.Field(ID, graphql_name='contentId')
    content_id_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='contentIdIn')
    content_id_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='contentIdNotIn')
    content_name = sgqlc.types.Field(String, graphql_name='contentName')
    content_parent = sgqlc.types.Field(Int, graphql_name='contentParent')
    content_status = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='contentStatus')
    content_type = sgqlc.types.Field(sgqlc.types.list_of(ContentTypeEnum), graphql_name='contentType')
    include_unapproved = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='includeUnapproved')
    karma = sgqlc.types.Field(Int, graphql_name='karma')
    order = sgqlc.types.Field(OrderEnum, graphql_name='order')
    orderby = sgqlc.types.Field(CommentsConnectionOrderbyEnum, graphql_name='orderby')
    parent = sgqlc.types.Field(Int, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    search = sgqlc.types.Field(String, graphql_name='search')
    status = sgqlc.types.Field(String, graphql_name='status')
    user_id = sgqlc.types.Field(ID, graphql_name='userId')


class ContentTypeToContentNodeConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('content_types', 'date_query', 'has_password', 'id', 'in_', 'mime_type', 'name', 'name_in', 'not_in', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'password', 'search', 'stati', 'status', 'title')
    content_types = sgqlc.types.Field(sgqlc.types.list_of(ContentTypeEnum), graphql_name='contentTypes')
    date_query = sgqlc.types.Field('DateQueryInput', graphql_name='dateQuery')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    id = sgqlc.types.Field(Int, graphql_name='id')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')
    mime_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='mimeType')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nameIn')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='notIn')
    orderby = sgqlc.types.Field(sgqlc.types.list_of('PostObjectsConnectionOrderbyInput'), graphql_name='orderby')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    password = sgqlc.types.Field(String, graphql_name='password')
    search = sgqlc.types.Field(String, graphql_name='search')
    stati = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='stati')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class ContractKindToContentNodeConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('content_types', 'date_query', 'has_password', 'id', 'in_', 'mime_type', 'name', 'name_in', 'not_in', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'password', 'search', 'stati', 'status', 'title')
    content_types = sgqlc.types.Field(sgqlc.types.list_of(ContentTypesOfContractKindEnum), graphql_name='contentTypes')
    date_query = sgqlc.types.Field('DateQueryInput', graphql_name='dateQuery')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    id = sgqlc.types.Field(Int, graphql_name='id')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')
    mime_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='mimeType')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nameIn')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='notIn')
    orderby = sgqlc.types.Field(sgqlc.types.list_of('PostObjectsConnectionOrderbyInput'), graphql_name='orderby')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    password = sgqlc.types.Field(String, graphql_name='password')
    search = sgqlc.types.Field(String, graphql_name='search')
    stati = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='stati')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class ContractKindToContractKindConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('cache_domain', 'child_of', 'childless', 'description_like', 'exclude', 'exclude_tree', 'hide_empty', 'hierarchical', 'include', 'name', 'name_like', 'object_ids', 'order', 'orderby', 'pad_counts', 'parent', 'search', 'slug', 'term_taxonom_id', 'term_taxonomy_id', 'update_term_meta_cache')
    cache_domain = sgqlc.types.Field(String, graphql_name='cacheDomain')
    child_of = sgqlc.types.Field(Int, graphql_name='childOf')
    childless = sgqlc.types.Field(Boolean, graphql_name='childless')
    description_like = sgqlc.types.Field(String, graphql_name='descriptionLike')
    exclude = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='exclude')
    exclude_tree = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='excludeTree')
    hide_empty = sgqlc.types.Field(Boolean, graphql_name='hideEmpty')
    hierarchical = sgqlc.types.Field(Boolean, graphql_name='hierarchical')
    include = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='include')
    name = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='name')
    name_like = sgqlc.types.Field(String, graphql_name='nameLike')
    object_ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='objectIds')
    order = sgqlc.types.Field(OrderEnum, graphql_name='order')
    orderby = sgqlc.types.Field(TermObjectsConnectionOrderbyEnum, graphql_name='orderby')
    pad_counts = sgqlc.types.Field(Boolean, graphql_name='padCounts')
    parent = sgqlc.types.Field(Int, graphql_name='parent')
    search = sgqlc.types.Field(String, graphql_name='search')
    slug = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='slug')
    term_taxonom_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomId')
    term_taxonomy_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomyId')
    update_term_meta_cache = sgqlc.types.Field(Boolean, graphql_name='updateTermMetaCache')


class ContractKindToJobConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author', 'author_in', 'author_name', 'author_not_in', 'date_query', 'has_password', 'id', 'in_', 'mime_type', 'name', 'name_in', 'not_in', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'password', 'search', 'stati', 'status', 'title')
    author = sgqlc.types.Field(Int, graphql_name='author')
    author_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorIn')
    author_name = sgqlc.types.Field(String, graphql_name='authorName')
    author_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorNotIn')
    date_query = sgqlc.types.Field('DateQueryInput', graphql_name='dateQuery')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    id = sgqlc.types.Field(Int, graphql_name='id')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')
    mime_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='mimeType')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nameIn')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='notIn')
    orderby = sgqlc.types.Field(sgqlc.types.list_of('PostObjectsConnectionOrderbyInput'), graphql_name='orderby')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    password = sgqlc.types.Field(String, graphql_name='password')
    search = sgqlc.types.Field(String, graphql_name='search')
    stati = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='stati')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class CreateCategoryInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('alias_of', 'client_mutation_id', 'description', 'name', 'parent_id', 'slug')
    alias_of = sgqlc.types.Field(String, graphql_name='aliasOf')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    description = sgqlc.types.Field(String, graphql_name='description')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    parent_id = sgqlc.types.Field(ID, graphql_name='parentId')
    slug = sgqlc.types.Field(String, graphql_name='slug')


class CreateCommentInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('approved', 'author', 'author_email', 'author_url', 'client_mutation_id', 'comment_on', 'content', 'date', 'parent', 'status', 'type')
    approved = sgqlc.types.Field(String, graphql_name='approved')
    author = sgqlc.types.Field(String, graphql_name='author')
    author_email = sgqlc.types.Field(String, graphql_name='authorEmail')
    author_url = sgqlc.types.Field(String, graphql_name='authorUrl')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    comment_on = sgqlc.types.Field(Int, graphql_name='commentOn')
    content = sgqlc.types.Field(String, graphql_name='content')
    date = sgqlc.types.Field(String, graphql_name='date')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    status = sgqlc.types.Field(CommentStatusEnum, graphql_name='status')
    type = sgqlc.types.Field(String, graphql_name='type')


class CreateContractKindInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('alias_of', 'client_mutation_id', 'description', 'name', 'parent_id', 'slug')
    alias_of = sgqlc.types.Field(String, graphql_name='aliasOf')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    description = sgqlc.types.Field(String, graphql_name='description')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    parent_id = sgqlc.types.Field(ID, graphql_name='parentId')
    slug = sgqlc.types.Field(String, graphql_name='slug')


class CreateEventInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('events_categories', 'author_id', 'client_mutation_id', 'comment_status', 'content', 'date', 'excerpt', 'menu_order', 'password', 'slug', 'status', 'tags', 'title')
    events_categories = sgqlc.types.Field('EventEventsCategoriesInput', graphql_name='eventsCategories')
    author_id = sgqlc.types.Field(ID, graphql_name='authorId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    comment_status = sgqlc.types.Field(String, graphql_name='commentStatus')
    content = sgqlc.types.Field(String, graphql_name='content')
    date = sgqlc.types.Field(String, graphql_name='date')
    excerpt = sgqlc.types.Field(String, graphql_name='excerpt')
    menu_order = sgqlc.types.Field(Int, graphql_name='menuOrder')
    password = sgqlc.types.Field(String, graphql_name='password')
    slug = sgqlc.types.Field(String, graphql_name='slug')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    tags = sgqlc.types.Field('EventTagsInput', graphql_name='tags')
    title = sgqlc.types.Field(String, graphql_name='title')


class CreateEventsCategoryInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('alias_of', 'client_mutation_id', 'description', 'name', 'parent_id', 'slug')
    alias_of = sgqlc.types.Field(String, graphql_name='aliasOf')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    description = sgqlc.types.Field(String, graphql_name='description')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    parent_id = sgqlc.types.Field(ID, graphql_name='parentId')
    slug = sgqlc.types.Field(String, graphql_name='slug')


class CreateGraphqlDocumentGroupInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('alias_of', 'client_mutation_id', 'description', 'name', 'slug')
    alias_of = sgqlc.types.Field(String, graphql_name='aliasOf')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    description = sgqlc.types.Field(String, graphql_name='description')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    slug = sgqlc.types.Field(String, graphql_name='slug')


class CreateGraphqlDocumentInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('alias', 'client_mutation_id', 'content', 'date', 'description', 'grant', 'graphql_document_groups', 'max_age_header', 'menu_order', 'password', 'slug', 'status', 'title')
    alias = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='alias')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    content = sgqlc.types.Field(String, graphql_name='content')
    date = sgqlc.types.Field(String, graphql_name='date')
    description = sgqlc.types.Field(String, graphql_name='description')
    grant = sgqlc.types.Field(String, graphql_name='grant')
    graphql_document_groups = sgqlc.types.Field('GraphqlDocumentGraphqlDocumentGroupsInput', graphql_name='graphqlDocumentGroups')
    max_age_header = sgqlc.types.Field(Int, graphql_name='maxAgeHeader')
    menu_order = sgqlc.types.Field(Int, graphql_name='menuOrder')
    password = sgqlc.types.Field(String, graphql_name='password')
    slug = sgqlc.types.Field(String, graphql_name='slug')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class CreateJobInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author_id', 'client_mutation_id', 'contractkinds', 'date', 'jobmodes', 'menu_order', 'occupationkinds', 'password', 'slug', 'status', 'title')
    author_id = sgqlc.types.Field(ID, graphql_name='authorId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    contractkinds = sgqlc.types.Field('JobContractkindsInput', graphql_name='contractkinds')
    date = sgqlc.types.Field(String, graphql_name='date')
    jobmodes = sgqlc.types.Field('JobJobmodesInput', graphql_name='jobmodes')
    menu_order = sgqlc.types.Field(Int, graphql_name='menuOrder')
    occupationkinds = sgqlc.types.Field('JobOccupationkindsInput', graphql_name='occupationkinds')
    password = sgqlc.types.Field(String, graphql_name='password')
    slug = sgqlc.types.Field(String, graphql_name='slug')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class CreateJobmodeInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('alias_of', 'client_mutation_id', 'description', 'name', 'slug')
    alias_of = sgqlc.types.Field(String, graphql_name='aliasOf')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    description = sgqlc.types.Field(String, graphql_name='description')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    slug = sgqlc.types.Field(String, graphql_name='slug')


class CreateMediaItemInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('alt_text', 'author_id', 'caption', 'client_mutation_id', 'comment_status', 'date', 'date_gmt', 'description', 'file_path', 'file_type', 'parent_id', 'ping_status', 'slug', 'status', 'title')
    alt_text = sgqlc.types.Field(String, graphql_name='altText')
    author_id = sgqlc.types.Field(ID, graphql_name='authorId')
    caption = sgqlc.types.Field(String, graphql_name='caption')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    comment_status = sgqlc.types.Field(String, graphql_name='commentStatus')
    date = sgqlc.types.Field(String, graphql_name='date')
    date_gmt = sgqlc.types.Field(String, graphql_name='dateGmt')
    description = sgqlc.types.Field(String, graphql_name='description')
    file_path = sgqlc.types.Field(String, graphql_name='filePath')
    file_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='fileType')
    parent_id = sgqlc.types.Field(ID, graphql_name='parentId')
    ping_status = sgqlc.types.Field(String, graphql_name='pingStatus')
    slug = sgqlc.types.Field(String, graphql_name='slug')
    status = sgqlc.types.Field(MediaItemStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class CreateOccupationkindInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('alias_of', 'client_mutation_id', 'description', 'name', 'slug')
    alias_of = sgqlc.types.Field(String, graphql_name='aliasOf')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    description = sgqlc.types.Field(String, graphql_name='description')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    slug = sgqlc.types.Field(String, graphql_name='slug')


class CreateOrganizerInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author_id', 'client_mutation_id', 'content', 'date', 'excerpt', 'menu_order', 'password', 'slug', 'status', 'title')
    author_id = sgqlc.types.Field(ID, graphql_name='authorId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    content = sgqlc.types.Field(String, graphql_name='content')
    date = sgqlc.types.Field(String, graphql_name='date')
    excerpt = sgqlc.types.Field(String, graphql_name='excerpt')
    menu_order = sgqlc.types.Field(Int, graphql_name='menuOrder')
    password = sgqlc.types.Field(String, graphql_name='password')
    slug = sgqlc.types.Field(String, graphql_name='slug')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class CreatePageInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author_id', 'client_mutation_id', 'comment_status', 'content', 'date', 'menu_order', 'parent_id', 'password', 'slug', 'status', 'title')
    author_id = sgqlc.types.Field(ID, graphql_name='authorId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    comment_status = sgqlc.types.Field(String, graphql_name='commentStatus')
    content = sgqlc.types.Field(String, graphql_name='content')
    date = sgqlc.types.Field(String, graphql_name='date')
    menu_order = sgqlc.types.Field(Int, graphql_name='menuOrder')
    parent_id = sgqlc.types.Field(ID, graphql_name='parentId')
    password = sgqlc.types.Field(String, graphql_name='password')
    slug = sgqlc.types.Field(String, graphql_name='slug')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class CreatePartnerInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author_id', 'client_mutation_id', 'date', 'menu_order', 'password', 'slug', 'status', 'title')
    author_id = sgqlc.types.Field(ID, graphql_name='authorId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    date = sgqlc.types.Field(String, graphql_name='date')
    menu_order = sgqlc.types.Field(Int, graphql_name='menuOrder')
    password = sgqlc.types.Field(String, graphql_name='password')
    slug = sgqlc.types.Field(String, graphql_name='slug')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class CreatePostFormatInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('alias_of', 'client_mutation_id', 'description', 'name', 'slug')
    alias_of = sgqlc.types.Field(String, graphql_name='aliasOf')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    description = sgqlc.types.Field(String, graphql_name='description')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    slug = sgqlc.types.Field(String, graphql_name='slug')


class CreatePostInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author_id', 'categories', 'client_mutation_id', 'comment_status', 'content', 'date', 'excerpt', 'menu_order', 'password', 'ping_status', 'pinged', 'post_formats', 'slug', 'status', 'tags', 'title', 'to_ping')
    author_id = sgqlc.types.Field(ID, graphql_name='authorId')
    categories = sgqlc.types.Field('PostCategoriesInput', graphql_name='categories')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    comment_status = sgqlc.types.Field(String, graphql_name='commentStatus')
    content = sgqlc.types.Field(String, graphql_name='content')
    date = sgqlc.types.Field(String, graphql_name='date')
    excerpt = sgqlc.types.Field(String, graphql_name='excerpt')
    menu_order = sgqlc.types.Field(Int, graphql_name='menuOrder')
    password = sgqlc.types.Field(String, graphql_name='password')
    ping_status = sgqlc.types.Field(String, graphql_name='pingStatus')
    pinged = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='pinged')
    post_formats = sgqlc.types.Field('PostPostFormatsInput', graphql_name='postFormats')
    slug = sgqlc.types.Field(String, graphql_name='slug')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    tags = sgqlc.types.Field('PostTagsInput', graphql_name='tags')
    title = sgqlc.types.Field(String, graphql_name='title')
    to_ping = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='toPing')


class CreateTagInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('alias_of', 'client_mutation_id', 'description', 'name', 'slug')
    alias_of = sgqlc.types.Field(String, graphql_name='aliasOf')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    description = sgqlc.types.Field(String, graphql_name='description')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    slug = sgqlc.types.Field(String, graphql_name='slug')


class CreateUserInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('aim', 'client_mutation_id', 'description', 'display_name', 'email', 'first_name', 'jabber', 'last_name', 'locale', 'nicename', 'nickname', 'password', 'refresh_jwt_user_secret', 'registered', 'revoke_jwt_user_secret', 'rich_editing', 'roles', 'username', 'website_url', 'yim')
    aim = sgqlc.types.Field(String, graphql_name='aim')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    description = sgqlc.types.Field(String, graphql_name='description')
    display_name = sgqlc.types.Field(String, graphql_name='displayName')
    email = sgqlc.types.Field(String, graphql_name='email')
    first_name = sgqlc.types.Field(String, graphql_name='firstName')
    jabber = sgqlc.types.Field(String, graphql_name='jabber')
    last_name = sgqlc.types.Field(String, graphql_name='lastName')
    locale = sgqlc.types.Field(String, graphql_name='locale')
    nicename = sgqlc.types.Field(String, graphql_name='nicename')
    nickname = sgqlc.types.Field(String, graphql_name='nickname')
    password = sgqlc.types.Field(String, graphql_name='password')
    refresh_jwt_user_secret = sgqlc.types.Field(Boolean, graphql_name='refreshJwtUserSecret')
    registered = sgqlc.types.Field(String, graphql_name='registered')
    revoke_jwt_user_secret = sgqlc.types.Field(Boolean, graphql_name='revokeJwtUserSecret')
    rich_editing = sgqlc.types.Field(String, graphql_name='richEditing')
    roles = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='roles')
    username = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='username')
    website_url = sgqlc.types.Field(String, graphql_name='websiteUrl')
    yim = sgqlc.types.Field(String, graphql_name='yim')


class CreateVenueInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author_id', 'client_mutation_id', 'content', 'date', 'excerpt', 'menu_order', 'password', 'slug', 'status', 'title')
    author_id = sgqlc.types.Field(ID, graphql_name='authorId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    content = sgqlc.types.Field(String, graphql_name='content')
    date = sgqlc.types.Field(String, graphql_name='date')
    excerpt = sgqlc.types.Field(String, graphql_name='excerpt')
    menu_order = sgqlc.types.Field(Int, graphql_name='menuOrder')
    password = sgqlc.types.Field(String, graphql_name='password')
    slug = sgqlc.types.Field(String, graphql_name='slug')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class DateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('day', 'month', 'year')
    day = sgqlc.types.Field(Int, graphql_name='day')
    month = sgqlc.types.Field(Int, graphql_name='month')
    year = sgqlc.types.Field(Int, graphql_name='year')


class DateQueryInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('after', 'before', 'column', 'compare', 'day', 'hour', 'inclusive', 'minute', 'month', 'relation', 'second', 'week', 'year')
    after = sgqlc.types.Field(DateInput, graphql_name='after')
    before = sgqlc.types.Field(DateInput, graphql_name='before')
    column = sgqlc.types.Field(PostObjectsConnectionDateColumnEnum, graphql_name='column')
    compare = sgqlc.types.Field(String, graphql_name='compare')
    day = sgqlc.types.Field(Int, graphql_name='day')
    hour = sgqlc.types.Field(Int, graphql_name='hour')
    inclusive = sgqlc.types.Field(Boolean, graphql_name='inclusive')
    minute = sgqlc.types.Field(Int, graphql_name='minute')
    month = sgqlc.types.Field(Int, graphql_name='month')
    relation = sgqlc.types.Field(RelationEnum, graphql_name='relation')
    second = sgqlc.types.Field(Int, graphql_name='second')
    week = sgqlc.types.Field(Int, graphql_name='week')
    year = sgqlc.types.Field(Int, graphql_name='year')


class DeleteCategoryInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class DeleteCommentInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'force_delete', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    force_delete = sgqlc.types.Field(Boolean, graphql_name='forceDelete')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class DeleteContractKindInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class DeleteEventInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'force_delete', 'id', 'ignore_edit_lock')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    force_delete = sgqlc.types.Field(Boolean, graphql_name='forceDelete')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    ignore_edit_lock = sgqlc.types.Field(Boolean, graphql_name='ignoreEditLock')


class DeleteEventsCategoryInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class DeleteGraphqlDocumentGroupInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class DeleteGraphqlDocumentInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'force_delete', 'id', 'ignore_edit_lock')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    force_delete = sgqlc.types.Field(Boolean, graphql_name='forceDelete')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    ignore_edit_lock = sgqlc.types.Field(Boolean, graphql_name='ignoreEditLock')


class DeleteJobInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'force_delete', 'id', 'ignore_edit_lock')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    force_delete = sgqlc.types.Field(Boolean, graphql_name='forceDelete')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    ignore_edit_lock = sgqlc.types.Field(Boolean, graphql_name='ignoreEditLock')


class DeleteJobmodeInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class DeleteMediaItemInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'force_delete', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    force_delete = sgqlc.types.Field(Boolean, graphql_name='forceDelete')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class DeleteOccupationkindInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class DeleteOrganizerInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'force_delete', 'id', 'ignore_edit_lock')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    force_delete = sgqlc.types.Field(Boolean, graphql_name='forceDelete')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    ignore_edit_lock = sgqlc.types.Field(Boolean, graphql_name='ignoreEditLock')


class DeletePageInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'force_delete', 'id', 'ignore_edit_lock')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    force_delete = sgqlc.types.Field(Boolean, graphql_name='forceDelete')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    ignore_edit_lock = sgqlc.types.Field(Boolean, graphql_name='ignoreEditLock')


class DeletePartnerInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'force_delete', 'id', 'ignore_edit_lock')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    force_delete = sgqlc.types.Field(Boolean, graphql_name='forceDelete')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    ignore_edit_lock = sgqlc.types.Field(Boolean, graphql_name='ignoreEditLock')


class DeletePostFormatInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class DeletePostInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'force_delete', 'id', 'ignore_edit_lock')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    force_delete = sgqlc.types.Field(Boolean, graphql_name='forceDelete')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    ignore_edit_lock = sgqlc.types.Field(Boolean, graphql_name='ignoreEditLock')


class DeleteTagInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class DeleteUserInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'id', 'reassign_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    reassign_id = sgqlc.types.Field(ID, graphql_name='reassignId')


class DeleteVenueInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'force_delete', 'id', 'ignore_edit_lock')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    force_delete = sgqlc.types.Field(Boolean, graphql_name='forceDelete')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    ignore_edit_lock = sgqlc.types.Field(Boolean, graphql_name='ignoreEditLock')


class EventEventsCategoriesInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('append', 'nodes')
    append = sgqlc.types.Field(Boolean, graphql_name='append')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('EventEventsCategoriesNodeInput'), graphql_name='nodes')


class EventEventsCategoriesNodeInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('description', 'id', 'name', 'slug')
    description = sgqlc.types.Field(String, graphql_name='description')
    id = sgqlc.types.Field(ID, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    slug = sgqlc.types.Field(String, graphql_name='slug')


class EventTagsInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('append', 'nodes')
    append = sgqlc.types.Field(Boolean, graphql_name='append')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('EventTagsNodeInput'), graphql_name='nodes')


class EventTagsNodeInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('description', 'id', 'name', 'slug')
    description = sgqlc.types.Field(String, graphql_name='description')
    id = sgqlc.types.Field(ID, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    slug = sgqlc.types.Field(String, graphql_name='slug')


class EventToCommentConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author_email', 'author_in', 'author_not_in', 'author_url', 'comment_in', 'comment_not_in', 'comment_type', 'comment_type_in', 'comment_type_not_in', 'content_author', 'content_author_in', 'content_author_not_in', 'content_id', 'content_id_in', 'content_id_not_in', 'content_name', 'content_parent', 'content_status', 'content_type', 'include_unapproved', 'karma', 'order', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'search', 'status', 'user_id')
    author_email = sgqlc.types.Field(String, graphql_name='authorEmail')
    author_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorIn')
    author_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorNotIn')
    author_url = sgqlc.types.Field(String, graphql_name='authorUrl')
    comment_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='commentIn')
    comment_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='commentNotIn')
    comment_type = sgqlc.types.Field(String, graphql_name='commentType')
    comment_type_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='commentTypeIn')
    comment_type_not_in = sgqlc.types.Field(String, graphql_name='commentTypeNotIn')
    content_author = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='contentAuthor')
    content_author_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='contentAuthorIn')
    content_author_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='contentAuthorNotIn')
    content_id = sgqlc.types.Field(ID, graphql_name='contentId')
    content_id_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='contentIdIn')
    content_id_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='contentIdNotIn')
    content_name = sgqlc.types.Field(String, graphql_name='contentName')
    content_parent = sgqlc.types.Field(Int, graphql_name='contentParent')
    content_status = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='contentStatus')
    content_type = sgqlc.types.Field(sgqlc.types.list_of(ContentTypeEnum), graphql_name='contentType')
    include_unapproved = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='includeUnapproved')
    karma = sgqlc.types.Field(Int, graphql_name='karma')
    order = sgqlc.types.Field(OrderEnum, graphql_name='order')
    orderby = sgqlc.types.Field(CommentsConnectionOrderbyEnum, graphql_name='orderby')
    parent = sgqlc.types.Field(Int, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    search = sgqlc.types.Field(String, graphql_name='search')
    status = sgqlc.types.Field(String, graphql_name='status')
    user_id = sgqlc.types.Field(ID, graphql_name='userId')


class EventToEventsCategoryConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('cache_domain', 'child_of', 'childless', 'description_like', 'exclude', 'exclude_tree', 'hide_empty', 'hierarchical', 'include', 'name', 'name_like', 'object_ids', 'order', 'orderby', 'pad_counts', 'parent', 'search', 'slug', 'term_taxonom_id', 'term_taxonomy_id', 'update_term_meta_cache')
    cache_domain = sgqlc.types.Field(String, graphql_name='cacheDomain')
    child_of = sgqlc.types.Field(Int, graphql_name='childOf')
    childless = sgqlc.types.Field(Boolean, graphql_name='childless')
    description_like = sgqlc.types.Field(String, graphql_name='descriptionLike')
    exclude = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='exclude')
    exclude_tree = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='excludeTree')
    hide_empty = sgqlc.types.Field(Boolean, graphql_name='hideEmpty')
    hierarchical = sgqlc.types.Field(Boolean, graphql_name='hierarchical')
    include = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='include')
    name = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='name')
    name_like = sgqlc.types.Field(String, graphql_name='nameLike')
    object_ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='objectIds')
    order = sgqlc.types.Field(OrderEnum, graphql_name='order')
    orderby = sgqlc.types.Field(TermObjectsConnectionOrderbyEnum, graphql_name='orderby')
    pad_counts = sgqlc.types.Field(Boolean, graphql_name='padCounts')
    parent = sgqlc.types.Field(Int, graphql_name='parent')
    search = sgqlc.types.Field(String, graphql_name='search')
    slug = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='slug')
    term_taxonom_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomId')
    term_taxonomy_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomyId')
    update_term_meta_cache = sgqlc.types.Field(Boolean, graphql_name='updateTermMetaCache')


class EventToOrganizerConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author', 'author_in', 'author_name', 'author_not_in', 'date_query', 'has_password', 'id', 'in_', 'mime_type', 'name', 'name_in', 'not_in', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'password', 'search', 'stati', 'status', 'title')
    author = sgqlc.types.Field(Int, graphql_name='author')
    author_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorIn')
    author_name = sgqlc.types.Field(String, graphql_name='authorName')
    author_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorNotIn')
    date_query = sgqlc.types.Field(DateQueryInput, graphql_name='dateQuery')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    id = sgqlc.types.Field(Int, graphql_name='id')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')
    mime_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='mimeType')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nameIn')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='notIn')
    orderby = sgqlc.types.Field(sgqlc.types.list_of('PostObjectsConnectionOrderbyInput'), graphql_name='orderby')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    password = sgqlc.types.Field(String, graphql_name='password')
    search = sgqlc.types.Field(String, graphql_name='search')
    stati = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='stati')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class EventToRevisionConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author', 'author_in', 'author_name', 'author_not_in', 'date_query', 'has_password', 'id', 'in_', 'mime_type', 'name', 'name_in', 'not_in', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'password', 'search', 'stati', 'status', 'tag', 'tag_id', 'tag_in', 'tag_not_in', 'tag_slug_and', 'tag_slug_in', 'title')
    author = sgqlc.types.Field(Int, graphql_name='author')
    author_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorIn')
    author_name = sgqlc.types.Field(String, graphql_name='authorName')
    author_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorNotIn')
    date_query = sgqlc.types.Field(DateQueryInput, graphql_name='dateQuery')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    id = sgqlc.types.Field(Int, graphql_name='id')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')
    mime_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='mimeType')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nameIn')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='notIn')
    orderby = sgqlc.types.Field(sgqlc.types.list_of('PostObjectsConnectionOrderbyInput'), graphql_name='orderby')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    password = sgqlc.types.Field(String, graphql_name='password')
    search = sgqlc.types.Field(String, graphql_name='search')
    stati = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='stati')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    tag = sgqlc.types.Field(String, graphql_name='tag')
    tag_id = sgqlc.types.Field(String, graphql_name='tagId')
    tag_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='tagIn')
    tag_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='tagNotIn')
    tag_slug_and = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tagSlugAnd')
    tag_slug_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tagSlugIn')
    title = sgqlc.types.Field(String, graphql_name='title')


class EventToTagConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('cache_domain', 'child_of', 'childless', 'description_like', 'exclude', 'exclude_tree', 'hide_empty', 'hierarchical', 'include', 'name', 'name_like', 'object_ids', 'order', 'orderby', 'pad_counts', 'parent', 'search', 'slug', 'term_taxonom_id', 'term_taxonomy_id', 'update_term_meta_cache')
    cache_domain = sgqlc.types.Field(String, graphql_name='cacheDomain')
    child_of = sgqlc.types.Field(Int, graphql_name='childOf')
    childless = sgqlc.types.Field(Boolean, graphql_name='childless')
    description_like = sgqlc.types.Field(String, graphql_name='descriptionLike')
    exclude = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='exclude')
    exclude_tree = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='excludeTree')
    hide_empty = sgqlc.types.Field(Boolean, graphql_name='hideEmpty')
    hierarchical = sgqlc.types.Field(Boolean, graphql_name='hierarchical')
    include = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='include')
    name = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='name')
    name_like = sgqlc.types.Field(String, graphql_name='nameLike')
    object_ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='objectIds')
    order = sgqlc.types.Field(OrderEnum, graphql_name='order')
    orderby = sgqlc.types.Field(TermObjectsConnectionOrderbyEnum, graphql_name='orderby')
    pad_counts = sgqlc.types.Field(Boolean, graphql_name='padCounts')
    parent = sgqlc.types.Field(Int, graphql_name='parent')
    search = sgqlc.types.Field(String, graphql_name='search')
    slug = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='slug')
    term_taxonom_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomId')
    term_taxonomy_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomyId')
    update_term_meta_cache = sgqlc.types.Field(Boolean, graphql_name='updateTermMetaCache')


class EventToTermNodeConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('cache_domain', 'child_of', 'childless', 'description_like', 'exclude', 'exclude_tree', 'hide_empty', 'hierarchical', 'include', 'name', 'name_like', 'object_ids', 'order', 'orderby', 'pad_counts', 'parent', 'search', 'slug', 'taxonomies', 'term_taxonom_id', 'term_taxonomy_id', 'update_term_meta_cache')
    cache_domain = sgqlc.types.Field(String, graphql_name='cacheDomain')
    child_of = sgqlc.types.Field(Int, graphql_name='childOf')
    childless = sgqlc.types.Field(Boolean, graphql_name='childless')
    description_like = sgqlc.types.Field(String, graphql_name='descriptionLike')
    exclude = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='exclude')
    exclude_tree = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='excludeTree')
    hide_empty = sgqlc.types.Field(Boolean, graphql_name='hideEmpty')
    hierarchical = sgqlc.types.Field(Boolean, graphql_name='hierarchical')
    include = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='include')
    name = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='name')
    name_like = sgqlc.types.Field(String, graphql_name='nameLike')
    object_ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='objectIds')
    order = sgqlc.types.Field(OrderEnum, graphql_name='order')
    orderby = sgqlc.types.Field(TermObjectsConnectionOrderbyEnum, graphql_name='orderby')
    pad_counts = sgqlc.types.Field(Boolean, graphql_name='padCounts')
    parent = sgqlc.types.Field(Int, graphql_name='parent')
    search = sgqlc.types.Field(String, graphql_name='search')
    slug = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='slug')
    taxonomies = sgqlc.types.Field(sgqlc.types.list_of(TaxonomyEnum), graphql_name='taxonomies')
    term_taxonom_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomId')
    term_taxonomy_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomyId')
    update_term_meta_cache = sgqlc.types.Field(Boolean, graphql_name='updateTermMetaCache')


class EventsCategoryToContentNodeConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('content_types', 'date_query', 'has_password', 'id', 'in_', 'mime_type', 'name', 'name_in', 'not_in', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'password', 'search', 'stati', 'status', 'title')
    content_types = sgqlc.types.Field(sgqlc.types.list_of(ContentTypesOfEventsCategoryEnum), graphql_name='contentTypes')
    date_query = sgqlc.types.Field(DateQueryInput, graphql_name='dateQuery')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    id = sgqlc.types.Field(Int, graphql_name='id')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')
    mime_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='mimeType')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nameIn')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='notIn')
    orderby = sgqlc.types.Field(sgqlc.types.list_of('PostObjectsConnectionOrderbyInput'), graphql_name='orderby')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    password = sgqlc.types.Field(String, graphql_name='password')
    search = sgqlc.types.Field(String, graphql_name='search')
    stati = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='stati')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class EventsCategoryToEventConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author', 'author_in', 'author_name', 'author_not_in', 'date_query', 'end_date_query', 'has_password', 'id', 'in_', 'mime_type', 'name', 'name_in', 'not_in', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'password', 'search', 'start_date_query', 'stati', 'status', 'tag', 'tag_id', 'tag_in', 'tag_not_in', 'tag_slug_and', 'tag_slug_in', 'title', 'venues_in', 'venues_not_in')
    author = sgqlc.types.Field(Int, graphql_name='author')
    author_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorIn')
    author_name = sgqlc.types.Field(String, graphql_name='authorName')
    author_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorNotIn')
    date_query = sgqlc.types.Field(DateQueryInput, graphql_name='dateQuery')
    end_date_query = sgqlc.types.Field(DateQueryInput, graphql_name='endDateQuery')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    id = sgqlc.types.Field(Int, graphql_name='id')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')
    mime_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='mimeType')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nameIn')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='notIn')
    orderby = sgqlc.types.Field(sgqlc.types.list_of('PostObjectsConnectionOrderbyInput'), graphql_name='orderby')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    password = sgqlc.types.Field(String, graphql_name='password')
    search = sgqlc.types.Field(String, graphql_name='search')
    start_date_query = sgqlc.types.Field(DateQueryInput, graphql_name='startDateQuery')
    stati = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='stati')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    tag = sgqlc.types.Field(String, graphql_name='tag')
    tag_id = sgqlc.types.Field(String, graphql_name='tagId')
    tag_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='tagIn')
    tag_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='tagNotIn')
    tag_slug_and = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tagSlugAnd')
    tag_slug_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tagSlugIn')
    title = sgqlc.types.Field(String, graphql_name='title')
    venues_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='venuesIn')
    venues_not_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='venuesNotIn')


class EventsCategoryToEventsCategoryConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('cache_domain', 'child_of', 'childless', 'description_like', 'exclude', 'exclude_tree', 'hide_empty', 'hierarchical', 'include', 'name', 'name_like', 'object_ids', 'order', 'orderby', 'pad_counts', 'parent', 'search', 'slug', 'term_taxonom_id', 'term_taxonomy_id', 'update_term_meta_cache')
    cache_domain = sgqlc.types.Field(String, graphql_name='cacheDomain')
    child_of = sgqlc.types.Field(Int, graphql_name='childOf')
    childless = sgqlc.types.Field(Boolean, graphql_name='childless')
    description_like = sgqlc.types.Field(String, graphql_name='descriptionLike')
    exclude = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='exclude')
    exclude_tree = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='excludeTree')
    hide_empty = sgqlc.types.Field(Boolean, graphql_name='hideEmpty')
    hierarchical = sgqlc.types.Field(Boolean, graphql_name='hierarchical')
    include = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='include')
    name = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='name')
    name_like = sgqlc.types.Field(String, graphql_name='nameLike')
    object_ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='objectIds')
    order = sgqlc.types.Field(OrderEnum, graphql_name='order')
    orderby = sgqlc.types.Field(TermObjectsConnectionOrderbyEnum, graphql_name='orderby')
    pad_counts = sgqlc.types.Field(Boolean, graphql_name='padCounts')
    parent = sgqlc.types.Field(Int, graphql_name='parent')
    search = sgqlc.types.Field(String, graphql_name='search')
    slug = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='slug')
    term_taxonom_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomId')
    term_taxonomy_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomyId')
    update_term_meta_cache = sgqlc.types.Field(Boolean, graphql_name='updateTermMetaCache')


class GraphqlDocumentGraphqlDocumentGroupsInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('append', 'nodes')
    append = sgqlc.types.Field(Boolean, graphql_name='append')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('GraphqlDocumentGraphqlDocumentGroupsNodeInput'), graphql_name='nodes')


class GraphqlDocumentGraphqlDocumentGroupsNodeInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('description', 'id', 'name', 'slug')
    description = sgqlc.types.Field(String, graphql_name='description')
    id = sgqlc.types.Field(ID, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    slug = sgqlc.types.Field(String, graphql_name='slug')


class GraphqlDocumentGroupToContentNodeConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('content_types', 'date_query', 'has_password', 'id', 'in_', 'mime_type', 'name', 'name_in', 'not_in', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'password', 'search', 'stati', 'status', 'title')
    content_types = sgqlc.types.Field(sgqlc.types.list_of(ContentTypesOfGraphqlDocumentGroupEnum), graphql_name='contentTypes')
    date_query = sgqlc.types.Field(DateQueryInput, graphql_name='dateQuery')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    id = sgqlc.types.Field(Int, graphql_name='id')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')
    mime_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='mimeType')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nameIn')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='notIn')
    orderby = sgqlc.types.Field(sgqlc.types.list_of('PostObjectsConnectionOrderbyInput'), graphql_name='orderby')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    password = sgqlc.types.Field(String, graphql_name='password')
    search = sgqlc.types.Field(String, graphql_name='search')
    stati = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='stati')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class GraphqlDocumentGroupToGraphqlDocumentConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('date_query', 'has_password', 'id', 'in_', 'mime_type', 'name', 'name_in', 'not_in', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'password', 'search', 'stati', 'status', 'title')
    date_query = sgqlc.types.Field(DateQueryInput, graphql_name='dateQuery')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    id = sgqlc.types.Field(Int, graphql_name='id')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')
    mime_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='mimeType')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nameIn')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='notIn')
    orderby = sgqlc.types.Field(sgqlc.types.list_of('PostObjectsConnectionOrderbyInput'), graphql_name='orderby')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    password = sgqlc.types.Field(String, graphql_name='password')
    search = sgqlc.types.Field(String, graphql_name='search')
    stati = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='stati')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class GraphqlDocumentToGraphqlDocumentGroupConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('cache_domain', 'child_of', 'childless', 'description_like', 'exclude', 'exclude_tree', 'hide_empty', 'hierarchical', 'include', 'name', 'name_like', 'object_ids', 'order', 'orderby', 'pad_counts', 'parent', 'search', 'slug', 'term_taxonom_id', 'term_taxonomy_id', 'update_term_meta_cache')
    cache_domain = sgqlc.types.Field(String, graphql_name='cacheDomain')
    child_of = sgqlc.types.Field(Int, graphql_name='childOf')
    childless = sgqlc.types.Field(Boolean, graphql_name='childless')
    description_like = sgqlc.types.Field(String, graphql_name='descriptionLike')
    exclude = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='exclude')
    exclude_tree = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='excludeTree')
    hide_empty = sgqlc.types.Field(Boolean, graphql_name='hideEmpty')
    hierarchical = sgqlc.types.Field(Boolean, graphql_name='hierarchical')
    include = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='include')
    name = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='name')
    name_like = sgqlc.types.Field(String, graphql_name='nameLike')
    object_ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='objectIds')
    order = sgqlc.types.Field(OrderEnum, graphql_name='order')
    orderby = sgqlc.types.Field(TermObjectsConnectionOrderbyEnum, graphql_name='orderby')
    pad_counts = sgqlc.types.Field(Boolean, graphql_name='padCounts')
    parent = sgqlc.types.Field(Int, graphql_name='parent')
    search = sgqlc.types.Field(String, graphql_name='search')
    slug = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='slug')
    term_taxonom_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomId')
    term_taxonomy_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomyId')
    update_term_meta_cache = sgqlc.types.Field(Boolean, graphql_name='updateTermMetaCache')


class GraphqlDocumentToTermNodeConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('cache_domain', 'child_of', 'childless', 'description_like', 'exclude', 'exclude_tree', 'hide_empty', 'hierarchical', 'include', 'name', 'name_like', 'object_ids', 'order', 'orderby', 'pad_counts', 'parent', 'search', 'slug', 'taxonomies', 'term_taxonom_id', 'term_taxonomy_id', 'update_term_meta_cache')
    cache_domain = sgqlc.types.Field(String, graphql_name='cacheDomain')
    child_of = sgqlc.types.Field(Int, graphql_name='childOf')
    childless = sgqlc.types.Field(Boolean, graphql_name='childless')
    description_like = sgqlc.types.Field(String, graphql_name='descriptionLike')
    exclude = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='exclude')
    exclude_tree = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='excludeTree')
    hide_empty = sgqlc.types.Field(Boolean, graphql_name='hideEmpty')
    hierarchical = sgqlc.types.Field(Boolean, graphql_name='hierarchical')
    include = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='include')
    name = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='name')
    name_like = sgqlc.types.Field(String, graphql_name='nameLike')
    object_ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='objectIds')
    order = sgqlc.types.Field(OrderEnum, graphql_name='order')
    orderby = sgqlc.types.Field(TermObjectsConnectionOrderbyEnum, graphql_name='orderby')
    pad_counts = sgqlc.types.Field(Boolean, graphql_name='padCounts')
    parent = sgqlc.types.Field(Int, graphql_name='parent')
    search = sgqlc.types.Field(String, graphql_name='search')
    slug = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='slug')
    taxonomies = sgqlc.types.Field(sgqlc.types.list_of(TaxonomyEnum), graphql_name='taxonomies')
    term_taxonom_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomId')
    term_taxonomy_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomyId')
    update_term_meta_cache = sgqlc.types.Field(Boolean, graphql_name='updateTermMetaCache')


class HierarchicalContentNodeToContentNodeAncestorsConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('content_types', 'date_query', 'has_password', 'id', 'in_', 'mime_type', 'name', 'name_in', 'not_in', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'password', 'search', 'stati', 'status', 'title')
    content_types = sgqlc.types.Field(sgqlc.types.list_of(ContentTypeEnum), graphql_name='contentTypes')
    date_query = sgqlc.types.Field(DateQueryInput, graphql_name='dateQuery')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    id = sgqlc.types.Field(Int, graphql_name='id')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')
    mime_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='mimeType')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nameIn')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='notIn')
    orderby = sgqlc.types.Field(sgqlc.types.list_of('PostObjectsConnectionOrderbyInput'), graphql_name='orderby')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    password = sgqlc.types.Field(String, graphql_name='password')
    search = sgqlc.types.Field(String, graphql_name='search')
    stati = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='stati')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class HierarchicalContentNodeToContentNodeChildrenConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('content_types', 'date_query', 'has_password', 'id', 'in_', 'mime_type', 'name', 'name_in', 'not_in', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'password', 'search', 'stati', 'status', 'title')
    content_types = sgqlc.types.Field(sgqlc.types.list_of(ContentTypeEnum), graphql_name='contentTypes')
    date_query = sgqlc.types.Field(DateQueryInput, graphql_name='dateQuery')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    id = sgqlc.types.Field(Int, graphql_name='id')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')
    mime_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='mimeType')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nameIn')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='notIn')
    orderby = sgqlc.types.Field(sgqlc.types.list_of('PostObjectsConnectionOrderbyInput'), graphql_name='orderby')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    password = sgqlc.types.Field(String, graphql_name='password')
    search = sgqlc.types.Field(String, graphql_name='search')
    stati = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='stati')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class JobContractkindsInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('append', 'nodes')
    append = sgqlc.types.Field(Boolean, graphql_name='append')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('JobContractkindsNodeInput'), graphql_name='nodes')


class JobContractkindsNodeInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('description', 'id', 'name', 'slug')
    description = sgqlc.types.Field(String, graphql_name='description')
    id = sgqlc.types.Field(ID, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    slug = sgqlc.types.Field(String, graphql_name='slug')


class JobJobmodesInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('append', 'nodes')
    append = sgqlc.types.Field(Boolean, graphql_name='append')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('JobJobmodesNodeInput'), graphql_name='nodes')


class JobJobmodesNodeInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('description', 'id', 'name', 'slug')
    description = sgqlc.types.Field(String, graphql_name='description')
    id = sgqlc.types.Field(ID, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    slug = sgqlc.types.Field(String, graphql_name='slug')


class JobOccupationkindsInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('append', 'nodes')
    append = sgqlc.types.Field(Boolean, graphql_name='append')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('JobOccupationkindsNodeInput'), graphql_name='nodes')


class JobOccupationkindsNodeInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('description', 'id', 'name', 'slug')
    description = sgqlc.types.Field(String, graphql_name='description')
    id = sgqlc.types.Field(ID, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    slug = sgqlc.types.Field(String, graphql_name='slug')


class JobToContractKindConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('cache_domain', 'child_of', 'childless', 'description_like', 'exclude', 'exclude_tree', 'hide_empty', 'hierarchical', 'include', 'name', 'name_like', 'object_ids', 'order', 'orderby', 'pad_counts', 'parent', 'search', 'slug', 'term_taxonom_id', 'term_taxonomy_id', 'update_term_meta_cache')
    cache_domain = sgqlc.types.Field(String, graphql_name='cacheDomain')
    child_of = sgqlc.types.Field(Int, graphql_name='childOf')
    childless = sgqlc.types.Field(Boolean, graphql_name='childless')
    description_like = sgqlc.types.Field(String, graphql_name='descriptionLike')
    exclude = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='exclude')
    exclude_tree = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='excludeTree')
    hide_empty = sgqlc.types.Field(Boolean, graphql_name='hideEmpty')
    hierarchical = sgqlc.types.Field(Boolean, graphql_name='hierarchical')
    include = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='include')
    name = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='name')
    name_like = sgqlc.types.Field(String, graphql_name='nameLike')
    object_ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='objectIds')
    order = sgqlc.types.Field(OrderEnum, graphql_name='order')
    orderby = sgqlc.types.Field(TermObjectsConnectionOrderbyEnum, graphql_name='orderby')
    pad_counts = sgqlc.types.Field(Boolean, graphql_name='padCounts')
    parent = sgqlc.types.Field(Int, graphql_name='parent')
    search = sgqlc.types.Field(String, graphql_name='search')
    slug = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='slug')
    term_taxonom_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomId')
    term_taxonomy_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomyId')
    update_term_meta_cache = sgqlc.types.Field(Boolean, graphql_name='updateTermMetaCache')


class JobToJobmodeConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('cache_domain', 'child_of', 'childless', 'description_like', 'exclude', 'exclude_tree', 'hide_empty', 'hierarchical', 'include', 'name', 'name_like', 'object_ids', 'order', 'orderby', 'pad_counts', 'parent', 'search', 'slug', 'term_taxonom_id', 'term_taxonomy_id', 'update_term_meta_cache')
    cache_domain = sgqlc.types.Field(String, graphql_name='cacheDomain')
    child_of = sgqlc.types.Field(Int, graphql_name='childOf')
    childless = sgqlc.types.Field(Boolean, graphql_name='childless')
    description_like = sgqlc.types.Field(String, graphql_name='descriptionLike')
    exclude = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='exclude')
    exclude_tree = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='excludeTree')
    hide_empty = sgqlc.types.Field(Boolean, graphql_name='hideEmpty')
    hierarchical = sgqlc.types.Field(Boolean, graphql_name='hierarchical')
    include = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='include')
    name = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='name')
    name_like = sgqlc.types.Field(String, graphql_name='nameLike')
    object_ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='objectIds')
    order = sgqlc.types.Field(OrderEnum, graphql_name='order')
    orderby = sgqlc.types.Field(TermObjectsConnectionOrderbyEnum, graphql_name='orderby')
    pad_counts = sgqlc.types.Field(Boolean, graphql_name='padCounts')
    parent = sgqlc.types.Field(Int, graphql_name='parent')
    search = sgqlc.types.Field(String, graphql_name='search')
    slug = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='slug')
    term_taxonom_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomId')
    term_taxonomy_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomyId')
    update_term_meta_cache = sgqlc.types.Field(Boolean, graphql_name='updateTermMetaCache')


class JobToOccupationkindConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('cache_domain', 'child_of', 'childless', 'description_like', 'exclude', 'exclude_tree', 'hide_empty', 'hierarchical', 'include', 'name', 'name_like', 'object_ids', 'order', 'orderby', 'pad_counts', 'parent', 'search', 'slug', 'term_taxonom_id', 'term_taxonomy_id', 'update_term_meta_cache')
    cache_domain = sgqlc.types.Field(String, graphql_name='cacheDomain')
    child_of = sgqlc.types.Field(Int, graphql_name='childOf')
    childless = sgqlc.types.Field(Boolean, graphql_name='childless')
    description_like = sgqlc.types.Field(String, graphql_name='descriptionLike')
    exclude = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='exclude')
    exclude_tree = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='excludeTree')
    hide_empty = sgqlc.types.Field(Boolean, graphql_name='hideEmpty')
    hierarchical = sgqlc.types.Field(Boolean, graphql_name='hierarchical')
    include = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='include')
    name = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='name')
    name_like = sgqlc.types.Field(String, graphql_name='nameLike')
    object_ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='objectIds')
    order = sgqlc.types.Field(OrderEnum, graphql_name='order')
    orderby = sgqlc.types.Field(TermObjectsConnectionOrderbyEnum, graphql_name='orderby')
    pad_counts = sgqlc.types.Field(Boolean, graphql_name='padCounts')
    parent = sgqlc.types.Field(Int, graphql_name='parent')
    search = sgqlc.types.Field(String, graphql_name='search')
    slug = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='slug')
    term_taxonom_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomId')
    term_taxonomy_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomyId')
    update_term_meta_cache = sgqlc.types.Field(Boolean, graphql_name='updateTermMetaCache')


class JobToTermNodeConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('cache_domain', 'child_of', 'childless', 'description_like', 'exclude', 'exclude_tree', 'hide_empty', 'hierarchical', 'include', 'name', 'name_like', 'object_ids', 'order', 'orderby', 'pad_counts', 'parent', 'search', 'slug', 'taxonomies', 'term_taxonom_id', 'term_taxonomy_id', 'update_term_meta_cache')
    cache_domain = sgqlc.types.Field(String, graphql_name='cacheDomain')
    child_of = sgqlc.types.Field(Int, graphql_name='childOf')
    childless = sgqlc.types.Field(Boolean, graphql_name='childless')
    description_like = sgqlc.types.Field(String, graphql_name='descriptionLike')
    exclude = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='exclude')
    exclude_tree = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='excludeTree')
    hide_empty = sgqlc.types.Field(Boolean, graphql_name='hideEmpty')
    hierarchical = sgqlc.types.Field(Boolean, graphql_name='hierarchical')
    include = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='include')
    name = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='name')
    name_like = sgqlc.types.Field(String, graphql_name='nameLike')
    object_ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='objectIds')
    order = sgqlc.types.Field(OrderEnum, graphql_name='order')
    orderby = sgqlc.types.Field(TermObjectsConnectionOrderbyEnum, graphql_name='orderby')
    pad_counts = sgqlc.types.Field(Boolean, graphql_name='padCounts')
    parent = sgqlc.types.Field(Int, graphql_name='parent')
    search = sgqlc.types.Field(String, graphql_name='search')
    slug = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='slug')
    taxonomies = sgqlc.types.Field(sgqlc.types.list_of(TaxonomyEnum), graphql_name='taxonomies')
    term_taxonom_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomId')
    term_taxonomy_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomyId')
    update_term_meta_cache = sgqlc.types.Field(Boolean, graphql_name='updateTermMetaCache')


class JobmodeToContentNodeConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('content_types', 'date_query', 'has_password', 'id', 'in_', 'mime_type', 'name', 'name_in', 'not_in', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'password', 'search', 'stati', 'status', 'title')
    content_types = sgqlc.types.Field(sgqlc.types.list_of(ContentTypesOfJobmodeEnum), graphql_name='contentTypes')
    date_query = sgqlc.types.Field(DateQueryInput, graphql_name='dateQuery')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    id = sgqlc.types.Field(Int, graphql_name='id')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')
    mime_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='mimeType')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nameIn')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='notIn')
    orderby = sgqlc.types.Field(sgqlc.types.list_of('PostObjectsConnectionOrderbyInput'), graphql_name='orderby')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    password = sgqlc.types.Field(String, graphql_name='password')
    search = sgqlc.types.Field(String, graphql_name='search')
    stati = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='stati')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class JobmodeToJobConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author', 'author_in', 'author_name', 'author_not_in', 'date_query', 'has_password', 'id', 'in_', 'mime_type', 'name', 'name_in', 'not_in', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'password', 'search', 'stati', 'status', 'title')
    author = sgqlc.types.Field(Int, graphql_name='author')
    author_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorIn')
    author_name = sgqlc.types.Field(String, graphql_name='authorName')
    author_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorNotIn')
    date_query = sgqlc.types.Field(DateQueryInput, graphql_name='dateQuery')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    id = sgqlc.types.Field(Int, graphql_name='id')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')
    mime_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='mimeType')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nameIn')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='notIn')
    orderby = sgqlc.types.Field(sgqlc.types.list_of('PostObjectsConnectionOrderbyInput'), graphql_name='orderby')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    password = sgqlc.types.Field(String, graphql_name='password')
    search = sgqlc.types.Field(String, graphql_name='search')
    stati = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='stati')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class LoginInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'password', 'username')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    password = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='password')
    username = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='username')


class MediaItemToCommentConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author_email', 'author_in', 'author_not_in', 'author_url', 'comment_in', 'comment_not_in', 'comment_type', 'comment_type_in', 'comment_type_not_in', 'content_author', 'content_author_in', 'content_author_not_in', 'content_id', 'content_id_in', 'content_id_not_in', 'content_name', 'content_parent', 'content_status', 'content_type', 'include_unapproved', 'karma', 'order', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'search', 'status', 'user_id')
    author_email = sgqlc.types.Field(String, graphql_name='authorEmail')
    author_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorIn')
    author_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorNotIn')
    author_url = sgqlc.types.Field(String, graphql_name='authorUrl')
    comment_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='commentIn')
    comment_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='commentNotIn')
    comment_type = sgqlc.types.Field(String, graphql_name='commentType')
    comment_type_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='commentTypeIn')
    comment_type_not_in = sgqlc.types.Field(String, graphql_name='commentTypeNotIn')
    content_author = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='contentAuthor')
    content_author_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='contentAuthorIn')
    content_author_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='contentAuthorNotIn')
    content_id = sgqlc.types.Field(ID, graphql_name='contentId')
    content_id_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='contentIdIn')
    content_id_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='contentIdNotIn')
    content_name = sgqlc.types.Field(String, graphql_name='contentName')
    content_parent = sgqlc.types.Field(Int, graphql_name='contentParent')
    content_status = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='contentStatus')
    content_type = sgqlc.types.Field(sgqlc.types.list_of(ContentTypeEnum), graphql_name='contentType')
    include_unapproved = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='includeUnapproved')
    karma = sgqlc.types.Field(Int, graphql_name='karma')
    order = sgqlc.types.Field(OrderEnum, graphql_name='order')
    orderby = sgqlc.types.Field(CommentsConnectionOrderbyEnum, graphql_name='orderby')
    parent = sgqlc.types.Field(Int, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    search = sgqlc.types.Field(String, graphql_name='search')
    status = sgqlc.types.Field(String, graphql_name='status')
    user_id = sgqlc.types.Field(ID, graphql_name='userId')


class MenuItemToMenuItemConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'location', 'parent_database_id', 'parent_id')
    id = sgqlc.types.Field(Int, graphql_name='id')
    location = sgqlc.types.Field(MenuLocationEnum, graphql_name='location')
    parent_database_id = sgqlc.types.Field(Int, graphql_name='parentDatabaseId')
    parent_id = sgqlc.types.Field(ID, graphql_name='parentId')


class MenuToMenuItemConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'location', 'parent_database_id', 'parent_id')
    id = sgqlc.types.Field(Int, graphql_name='id')
    location = sgqlc.types.Field(MenuLocationEnum, graphql_name='location')
    parent_database_id = sgqlc.types.Field(Int, graphql_name='parentDatabaseId')
    parent_id = sgqlc.types.Field(ID, graphql_name='parentId')


class OccupationkindToContentNodeConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('content_types', 'date_query', 'has_password', 'id', 'in_', 'mime_type', 'name', 'name_in', 'not_in', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'password', 'search', 'stati', 'status', 'title')
    content_types = sgqlc.types.Field(sgqlc.types.list_of(ContentTypesOfOccupationkindEnum), graphql_name='contentTypes')
    date_query = sgqlc.types.Field(DateQueryInput, graphql_name='dateQuery')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    id = sgqlc.types.Field(Int, graphql_name='id')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')
    mime_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='mimeType')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nameIn')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='notIn')
    orderby = sgqlc.types.Field(sgqlc.types.list_of('PostObjectsConnectionOrderbyInput'), graphql_name='orderby')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    password = sgqlc.types.Field(String, graphql_name='password')
    search = sgqlc.types.Field(String, graphql_name='search')
    stati = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='stati')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class OccupationkindToJobConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author', 'author_in', 'author_name', 'author_not_in', 'date_query', 'has_password', 'id', 'in_', 'mime_type', 'name', 'name_in', 'not_in', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'password', 'search', 'stati', 'status', 'title')
    author = sgqlc.types.Field(Int, graphql_name='author')
    author_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorIn')
    author_name = sgqlc.types.Field(String, graphql_name='authorName')
    author_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorNotIn')
    date_query = sgqlc.types.Field(DateQueryInput, graphql_name='dateQuery')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    id = sgqlc.types.Field(Int, graphql_name='id')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')
    mime_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='mimeType')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nameIn')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='notIn')
    orderby = sgqlc.types.Field(sgqlc.types.list_of('PostObjectsConnectionOrderbyInput'), graphql_name='orderby')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    password = sgqlc.types.Field(String, graphql_name='password')
    search = sgqlc.types.Field(String, graphql_name='search')
    stati = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='stati')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class OrganizerToRevisionConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author', 'author_in', 'author_name', 'author_not_in', 'date_query', 'has_password', 'id', 'in_', 'mime_type', 'name', 'name_in', 'not_in', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'password', 'search', 'stati', 'status', 'title')
    author = sgqlc.types.Field(Int, graphql_name='author')
    author_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorIn')
    author_name = sgqlc.types.Field(String, graphql_name='authorName')
    author_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorNotIn')
    date_query = sgqlc.types.Field(DateQueryInput, graphql_name='dateQuery')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    id = sgqlc.types.Field(Int, graphql_name='id')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')
    mime_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='mimeType')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nameIn')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='notIn')
    orderby = sgqlc.types.Field(sgqlc.types.list_of('PostObjectsConnectionOrderbyInput'), graphql_name='orderby')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    password = sgqlc.types.Field(String, graphql_name='password')
    search = sgqlc.types.Field(String, graphql_name='search')
    stati = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='stati')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class PageToCommentConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author_email', 'author_in', 'author_not_in', 'author_url', 'comment_in', 'comment_not_in', 'comment_type', 'comment_type_in', 'comment_type_not_in', 'content_author', 'content_author_in', 'content_author_not_in', 'content_id', 'content_id_in', 'content_id_not_in', 'content_name', 'content_parent', 'content_status', 'content_type', 'include_unapproved', 'karma', 'order', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'search', 'status', 'user_id')
    author_email = sgqlc.types.Field(String, graphql_name='authorEmail')
    author_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorIn')
    author_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorNotIn')
    author_url = sgqlc.types.Field(String, graphql_name='authorUrl')
    comment_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='commentIn')
    comment_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='commentNotIn')
    comment_type = sgqlc.types.Field(String, graphql_name='commentType')
    comment_type_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='commentTypeIn')
    comment_type_not_in = sgqlc.types.Field(String, graphql_name='commentTypeNotIn')
    content_author = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='contentAuthor')
    content_author_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='contentAuthorIn')
    content_author_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='contentAuthorNotIn')
    content_id = sgqlc.types.Field(ID, graphql_name='contentId')
    content_id_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='contentIdIn')
    content_id_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='contentIdNotIn')
    content_name = sgqlc.types.Field(String, graphql_name='contentName')
    content_parent = sgqlc.types.Field(Int, graphql_name='contentParent')
    content_status = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='contentStatus')
    content_type = sgqlc.types.Field(sgqlc.types.list_of(ContentTypeEnum), graphql_name='contentType')
    include_unapproved = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='includeUnapproved')
    karma = sgqlc.types.Field(Int, graphql_name='karma')
    order = sgqlc.types.Field(OrderEnum, graphql_name='order')
    orderby = sgqlc.types.Field(CommentsConnectionOrderbyEnum, graphql_name='orderby')
    parent = sgqlc.types.Field(Int, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    search = sgqlc.types.Field(String, graphql_name='search')
    status = sgqlc.types.Field(String, graphql_name='status')
    user_id = sgqlc.types.Field(ID, graphql_name='userId')


class PageToRevisionConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author', 'author_in', 'author_name', 'author_not_in', 'date_query', 'has_password', 'id', 'in_', 'mime_type', 'name', 'name_in', 'not_in', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'password', 'search', 'stati', 'status', 'title')
    author = sgqlc.types.Field(Int, graphql_name='author')
    author_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorIn')
    author_name = sgqlc.types.Field(String, graphql_name='authorName')
    author_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorNotIn')
    date_query = sgqlc.types.Field(DateQueryInput, graphql_name='dateQuery')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    id = sgqlc.types.Field(Int, graphql_name='id')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')
    mime_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='mimeType')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nameIn')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='notIn')
    orderby = sgqlc.types.Field(sgqlc.types.list_of('PostObjectsConnectionOrderbyInput'), graphql_name='orderby')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    password = sgqlc.types.Field(String, graphql_name='password')
    search = sgqlc.types.Field(String, graphql_name='search')
    stati = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='stati')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class PostCategoriesInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('append', 'nodes')
    append = sgqlc.types.Field(Boolean, graphql_name='append')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('PostCategoriesNodeInput'), graphql_name='nodes')


class PostCategoriesNodeInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('description', 'id', 'name', 'slug')
    description = sgqlc.types.Field(String, graphql_name='description')
    id = sgqlc.types.Field(ID, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    slug = sgqlc.types.Field(String, graphql_name='slug')


class PostFormatToContentNodeConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('content_types', 'date_query', 'has_password', 'id', 'in_', 'mime_type', 'name', 'name_in', 'not_in', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'password', 'search', 'stati', 'status', 'title')
    content_types = sgqlc.types.Field(sgqlc.types.list_of(ContentTypesOfPostFormatEnum), graphql_name='contentTypes')
    date_query = sgqlc.types.Field(DateQueryInput, graphql_name='dateQuery')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    id = sgqlc.types.Field(Int, graphql_name='id')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')
    mime_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='mimeType')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nameIn')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='notIn')
    orderby = sgqlc.types.Field(sgqlc.types.list_of('PostObjectsConnectionOrderbyInput'), graphql_name='orderby')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    password = sgqlc.types.Field(String, graphql_name='password')
    search = sgqlc.types.Field(String, graphql_name='search')
    stati = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='stati')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class PostFormatToPostConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author', 'author_in', 'author_name', 'author_not_in', 'category_id', 'category_in', 'category_name', 'category_not_in', 'date_query', 'has_password', 'id', 'in_', 'mime_type', 'name', 'name_in', 'not_in', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'password', 'search', 'stati', 'status', 'tag', 'tag_id', 'tag_in', 'tag_not_in', 'tag_slug_and', 'tag_slug_in', 'title')
    author = sgqlc.types.Field(Int, graphql_name='author')
    author_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorIn')
    author_name = sgqlc.types.Field(String, graphql_name='authorName')
    author_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorNotIn')
    category_id = sgqlc.types.Field(Int, graphql_name='categoryId')
    category_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='categoryIn')
    category_name = sgqlc.types.Field(String, graphql_name='categoryName')
    category_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='categoryNotIn')
    date_query = sgqlc.types.Field(DateQueryInput, graphql_name='dateQuery')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    id = sgqlc.types.Field(Int, graphql_name='id')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')
    mime_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='mimeType')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nameIn')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='notIn')
    orderby = sgqlc.types.Field(sgqlc.types.list_of('PostObjectsConnectionOrderbyInput'), graphql_name='orderby')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    password = sgqlc.types.Field(String, graphql_name='password')
    search = sgqlc.types.Field(String, graphql_name='search')
    stati = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='stati')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    tag = sgqlc.types.Field(String, graphql_name='tag')
    tag_id = sgqlc.types.Field(String, graphql_name='tagId')
    tag_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='tagIn')
    tag_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='tagNotIn')
    tag_slug_and = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tagSlugAnd')
    tag_slug_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tagSlugIn')
    title = sgqlc.types.Field(String, graphql_name='title')


class PostObjectsConnectionOrderbyInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'order')
    field = sgqlc.types.Field(sgqlc.types.non_null(PostObjectsConnectionOrderbyEnum), graphql_name='field')
    order = sgqlc.types.Field(sgqlc.types.non_null(OrderEnum), graphql_name='order')


class PostPostFormatsInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('append', 'nodes')
    append = sgqlc.types.Field(Boolean, graphql_name='append')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('PostPostFormatsNodeInput'), graphql_name='nodes')


class PostPostFormatsNodeInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('description', 'id', 'name', 'slug')
    description = sgqlc.types.Field(String, graphql_name='description')
    id = sgqlc.types.Field(ID, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    slug = sgqlc.types.Field(String, graphql_name='slug')


class PostTagsInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('append', 'nodes')
    append = sgqlc.types.Field(Boolean, graphql_name='append')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('PostTagsNodeInput'), graphql_name='nodes')


class PostTagsNodeInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('description', 'id', 'name', 'slug')
    description = sgqlc.types.Field(String, graphql_name='description')
    id = sgqlc.types.Field(ID, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    slug = sgqlc.types.Field(String, graphql_name='slug')


class PostToCategoryConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('cache_domain', 'child_of', 'childless', 'description_like', 'exclude', 'exclude_tree', 'hide_empty', 'hierarchical', 'include', 'name', 'name_like', 'object_ids', 'order', 'orderby', 'pad_counts', 'parent', 'search', 'slug', 'term_taxonom_id', 'term_taxonomy_id', 'update_term_meta_cache')
    cache_domain = sgqlc.types.Field(String, graphql_name='cacheDomain')
    child_of = sgqlc.types.Field(Int, graphql_name='childOf')
    childless = sgqlc.types.Field(Boolean, graphql_name='childless')
    description_like = sgqlc.types.Field(String, graphql_name='descriptionLike')
    exclude = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='exclude')
    exclude_tree = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='excludeTree')
    hide_empty = sgqlc.types.Field(Boolean, graphql_name='hideEmpty')
    hierarchical = sgqlc.types.Field(Boolean, graphql_name='hierarchical')
    include = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='include')
    name = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='name')
    name_like = sgqlc.types.Field(String, graphql_name='nameLike')
    object_ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='objectIds')
    order = sgqlc.types.Field(OrderEnum, graphql_name='order')
    orderby = sgqlc.types.Field(TermObjectsConnectionOrderbyEnum, graphql_name='orderby')
    pad_counts = sgqlc.types.Field(Boolean, graphql_name='padCounts')
    parent = sgqlc.types.Field(Int, graphql_name='parent')
    search = sgqlc.types.Field(String, graphql_name='search')
    slug = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='slug')
    term_taxonom_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomId')
    term_taxonomy_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomyId')
    update_term_meta_cache = sgqlc.types.Field(Boolean, graphql_name='updateTermMetaCache')


class PostToCommentConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author_email', 'author_in', 'author_not_in', 'author_url', 'comment_in', 'comment_not_in', 'comment_type', 'comment_type_in', 'comment_type_not_in', 'content_author', 'content_author_in', 'content_author_not_in', 'content_id', 'content_id_in', 'content_id_not_in', 'content_name', 'content_parent', 'content_status', 'content_type', 'include_unapproved', 'karma', 'order', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'search', 'status', 'user_id')
    author_email = sgqlc.types.Field(String, graphql_name='authorEmail')
    author_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorIn')
    author_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorNotIn')
    author_url = sgqlc.types.Field(String, graphql_name='authorUrl')
    comment_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='commentIn')
    comment_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='commentNotIn')
    comment_type = sgqlc.types.Field(String, graphql_name='commentType')
    comment_type_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='commentTypeIn')
    comment_type_not_in = sgqlc.types.Field(String, graphql_name='commentTypeNotIn')
    content_author = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='contentAuthor')
    content_author_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='contentAuthorIn')
    content_author_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='contentAuthorNotIn')
    content_id = sgqlc.types.Field(ID, graphql_name='contentId')
    content_id_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='contentIdIn')
    content_id_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='contentIdNotIn')
    content_name = sgqlc.types.Field(String, graphql_name='contentName')
    content_parent = sgqlc.types.Field(Int, graphql_name='contentParent')
    content_status = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='contentStatus')
    content_type = sgqlc.types.Field(sgqlc.types.list_of(ContentTypeEnum), graphql_name='contentType')
    include_unapproved = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='includeUnapproved')
    karma = sgqlc.types.Field(Int, graphql_name='karma')
    order = sgqlc.types.Field(OrderEnum, graphql_name='order')
    orderby = sgqlc.types.Field(CommentsConnectionOrderbyEnum, graphql_name='orderby')
    parent = sgqlc.types.Field(Int, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    search = sgqlc.types.Field(String, graphql_name='search')
    status = sgqlc.types.Field(String, graphql_name='status')
    user_id = sgqlc.types.Field(ID, graphql_name='userId')


class PostToPostFormatConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('cache_domain', 'child_of', 'childless', 'description_like', 'exclude', 'exclude_tree', 'hide_empty', 'hierarchical', 'include', 'name', 'name_like', 'object_ids', 'order', 'orderby', 'pad_counts', 'parent', 'search', 'slug', 'term_taxonom_id', 'term_taxonomy_id', 'update_term_meta_cache')
    cache_domain = sgqlc.types.Field(String, graphql_name='cacheDomain')
    child_of = sgqlc.types.Field(Int, graphql_name='childOf')
    childless = sgqlc.types.Field(Boolean, graphql_name='childless')
    description_like = sgqlc.types.Field(String, graphql_name='descriptionLike')
    exclude = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='exclude')
    exclude_tree = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='excludeTree')
    hide_empty = sgqlc.types.Field(Boolean, graphql_name='hideEmpty')
    hierarchical = sgqlc.types.Field(Boolean, graphql_name='hierarchical')
    include = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='include')
    name = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='name')
    name_like = sgqlc.types.Field(String, graphql_name='nameLike')
    object_ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='objectIds')
    order = sgqlc.types.Field(OrderEnum, graphql_name='order')
    orderby = sgqlc.types.Field(TermObjectsConnectionOrderbyEnum, graphql_name='orderby')
    pad_counts = sgqlc.types.Field(Boolean, graphql_name='padCounts')
    parent = sgqlc.types.Field(Int, graphql_name='parent')
    search = sgqlc.types.Field(String, graphql_name='search')
    slug = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='slug')
    term_taxonom_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomId')
    term_taxonomy_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomyId')
    update_term_meta_cache = sgqlc.types.Field(Boolean, graphql_name='updateTermMetaCache')


class PostToRevisionConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author', 'author_in', 'author_name', 'author_not_in', 'category_id', 'category_in', 'category_name', 'category_not_in', 'date_query', 'has_password', 'id', 'in_', 'mime_type', 'name', 'name_in', 'not_in', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'password', 'search', 'stati', 'status', 'tag', 'tag_id', 'tag_in', 'tag_not_in', 'tag_slug_and', 'tag_slug_in', 'title')
    author = sgqlc.types.Field(Int, graphql_name='author')
    author_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorIn')
    author_name = sgqlc.types.Field(String, graphql_name='authorName')
    author_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorNotIn')
    category_id = sgqlc.types.Field(Int, graphql_name='categoryId')
    category_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='categoryIn')
    category_name = sgqlc.types.Field(String, graphql_name='categoryName')
    category_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='categoryNotIn')
    date_query = sgqlc.types.Field(DateQueryInput, graphql_name='dateQuery')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    id = sgqlc.types.Field(Int, graphql_name='id')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')
    mime_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='mimeType')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nameIn')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='notIn')
    orderby = sgqlc.types.Field(sgqlc.types.list_of(PostObjectsConnectionOrderbyInput), graphql_name='orderby')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    password = sgqlc.types.Field(String, graphql_name='password')
    search = sgqlc.types.Field(String, graphql_name='search')
    stati = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='stati')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    tag = sgqlc.types.Field(String, graphql_name='tag')
    tag_id = sgqlc.types.Field(String, graphql_name='tagId')
    tag_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='tagIn')
    tag_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='tagNotIn')
    tag_slug_and = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tagSlugAnd')
    tag_slug_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tagSlugIn')
    title = sgqlc.types.Field(String, graphql_name='title')


class PostToTagConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('cache_domain', 'child_of', 'childless', 'description_like', 'exclude', 'exclude_tree', 'hide_empty', 'hierarchical', 'include', 'name', 'name_like', 'object_ids', 'order', 'orderby', 'pad_counts', 'parent', 'search', 'slug', 'term_taxonom_id', 'term_taxonomy_id', 'update_term_meta_cache')
    cache_domain = sgqlc.types.Field(String, graphql_name='cacheDomain')
    child_of = sgqlc.types.Field(Int, graphql_name='childOf')
    childless = sgqlc.types.Field(Boolean, graphql_name='childless')
    description_like = sgqlc.types.Field(String, graphql_name='descriptionLike')
    exclude = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='exclude')
    exclude_tree = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='excludeTree')
    hide_empty = sgqlc.types.Field(Boolean, graphql_name='hideEmpty')
    hierarchical = sgqlc.types.Field(Boolean, graphql_name='hierarchical')
    include = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='include')
    name = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='name')
    name_like = sgqlc.types.Field(String, graphql_name='nameLike')
    object_ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='objectIds')
    order = sgqlc.types.Field(OrderEnum, graphql_name='order')
    orderby = sgqlc.types.Field(TermObjectsConnectionOrderbyEnum, graphql_name='orderby')
    pad_counts = sgqlc.types.Field(Boolean, graphql_name='padCounts')
    parent = sgqlc.types.Field(Int, graphql_name='parent')
    search = sgqlc.types.Field(String, graphql_name='search')
    slug = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='slug')
    term_taxonom_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomId')
    term_taxonomy_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomyId')
    update_term_meta_cache = sgqlc.types.Field(Boolean, graphql_name='updateTermMetaCache')


class PostToTermNodeConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('cache_domain', 'child_of', 'childless', 'description_like', 'exclude', 'exclude_tree', 'hide_empty', 'hierarchical', 'include', 'name', 'name_like', 'object_ids', 'order', 'orderby', 'pad_counts', 'parent', 'search', 'slug', 'taxonomies', 'term_taxonom_id', 'term_taxonomy_id', 'update_term_meta_cache')
    cache_domain = sgqlc.types.Field(String, graphql_name='cacheDomain')
    child_of = sgqlc.types.Field(Int, graphql_name='childOf')
    childless = sgqlc.types.Field(Boolean, graphql_name='childless')
    description_like = sgqlc.types.Field(String, graphql_name='descriptionLike')
    exclude = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='exclude')
    exclude_tree = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='excludeTree')
    hide_empty = sgqlc.types.Field(Boolean, graphql_name='hideEmpty')
    hierarchical = sgqlc.types.Field(Boolean, graphql_name='hierarchical')
    include = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='include')
    name = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='name')
    name_like = sgqlc.types.Field(String, graphql_name='nameLike')
    object_ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='objectIds')
    order = sgqlc.types.Field(OrderEnum, graphql_name='order')
    orderby = sgqlc.types.Field(TermObjectsConnectionOrderbyEnum, graphql_name='orderby')
    pad_counts = sgqlc.types.Field(Boolean, graphql_name='padCounts')
    parent = sgqlc.types.Field(Int, graphql_name='parent')
    search = sgqlc.types.Field(String, graphql_name='search')
    slug = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='slug')
    taxonomies = sgqlc.types.Field(sgqlc.types.list_of(TaxonomyEnum), graphql_name='taxonomies')
    term_taxonom_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomId')
    term_taxonomy_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomyId')
    update_term_meta_cache = sgqlc.types.Field(Boolean, graphql_name='updateTermMetaCache')


class RefreshJwtAuthTokenInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'jwt_refresh_token')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    jwt_refresh_token = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='jwtRefreshToken')


class RegisterUserInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('aim', 'client_mutation_id', 'description', 'display_name', 'email', 'first_name', 'jabber', 'last_name', 'locale', 'nicename', 'nickname', 'password', 'refresh_jwt_user_secret', 'registered', 'revoke_jwt_user_secret', 'rich_editing', 'username', 'website_url', 'yim')
    aim = sgqlc.types.Field(String, graphql_name='aim')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    description = sgqlc.types.Field(String, graphql_name='description')
    display_name = sgqlc.types.Field(String, graphql_name='displayName')
    email = sgqlc.types.Field(String, graphql_name='email')
    first_name = sgqlc.types.Field(String, graphql_name='firstName')
    jabber = sgqlc.types.Field(String, graphql_name='jabber')
    last_name = sgqlc.types.Field(String, graphql_name='lastName')
    locale = sgqlc.types.Field(String, graphql_name='locale')
    nicename = sgqlc.types.Field(String, graphql_name='nicename')
    nickname = sgqlc.types.Field(String, graphql_name='nickname')
    password = sgqlc.types.Field(String, graphql_name='password')
    refresh_jwt_user_secret = sgqlc.types.Field(Boolean, graphql_name='refreshJwtUserSecret')
    registered = sgqlc.types.Field(String, graphql_name='registered')
    revoke_jwt_user_secret = sgqlc.types.Field(Boolean, graphql_name='revokeJwtUserSecret')
    rich_editing = sgqlc.types.Field(String, graphql_name='richEditing')
    username = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='username')
    website_url = sgqlc.types.Field(String, graphql_name='websiteUrl')
    yim = sgqlc.types.Field(String, graphql_name='yim')


class ResetUserPasswordInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'key', 'login', 'password')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    key = sgqlc.types.Field(String, graphql_name='key')
    login = sgqlc.types.Field(String, graphql_name='login')
    password = sgqlc.types.Field(String, graphql_name='password')


class RestoreCommentInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class RootQueryToCategoryConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('cache_domain', 'child_of', 'childless', 'description_like', 'exclude', 'exclude_tree', 'hide_empty', 'hierarchical', 'include', 'name', 'name_like', 'object_ids', 'order', 'orderby', 'pad_counts', 'parent', 'search', 'slug', 'term_taxonom_id', 'term_taxonomy_id', 'update_term_meta_cache')
    cache_domain = sgqlc.types.Field(String, graphql_name='cacheDomain')
    child_of = sgqlc.types.Field(Int, graphql_name='childOf')
    childless = sgqlc.types.Field(Boolean, graphql_name='childless')
    description_like = sgqlc.types.Field(String, graphql_name='descriptionLike')
    exclude = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='exclude')
    exclude_tree = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='excludeTree')
    hide_empty = sgqlc.types.Field(Boolean, graphql_name='hideEmpty')
    hierarchical = sgqlc.types.Field(Boolean, graphql_name='hierarchical')
    include = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='include')
    name = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='name')
    name_like = sgqlc.types.Field(String, graphql_name='nameLike')
    object_ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='objectIds')
    order = sgqlc.types.Field(OrderEnum, graphql_name='order')
    orderby = sgqlc.types.Field(TermObjectsConnectionOrderbyEnum, graphql_name='orderby')
    pad_counts = sgqlc.types.Field(Boolean, graphql_name='padCounts')
    parent = sgqlc.types.Field(Int, graphql_name='parent')
    search = sgqlc.types.Field(String, graphql_name='search')
    slug = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='slug')
    term_taxonom_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomId')
    term_taxonomy_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomyId')
    update_term_meta_cache = sgqlc.types.Field(Boolean, graphql_name='updateTermMetaCache')


class RootQueryToCommentConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author_email', 'author_in', 'author_not_in', 'author_url', 'comment_in', 'comment_not_in', 'comment_type', 'comment_type_in', 'comment_type_not_in', 'content_author', 'content_author_in', 'content_author_not_in', 'content_id', 'content_id_in', 'content_id_not_in', 'content_name', 'content_parent', 'content_status', 'content_type', 'include_unapproved', 'karma', 'order', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'search', 'status', 'user_id')
    author_email = sgqlc.types.Field(String, graphql_name='authorEmail')
    author_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorIn')
    author_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorNotIn')
    author_url = sgqlc.types.Field(String, graphql_name='authorUrl')
    comment_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='commentIn')
    comment_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='commentNotIn')
    comment_type = sgqlc.types.Field(String, graphql_name='commentType')
    comment_type_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='commentTypeIn')
    comment_type_not_in = sgqlc.types.Field(String, graphql_name='commentTypeNotIn')
    content_author = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='contentAuthor')
    content_author_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='contentAuthorIn')
    content_author_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='contentAuthorNotIn')
    content_id = sgqlc.types.Field(ID, graphql_name='contentId')
    content_id_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='contentIdIn')
    content_id_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='contentIdNotIn')
    content_name = sgqlc.types.Field(String, graphql_name='contentName')
    content_parent = sgqlc.types.Field(Int, graphql_name='contentParent')
    content_status = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='contentStatus')
    content_type = sgqlc.types.Field(sgqlc.types.list_of(ContentTypeEnum), graphql_name='contentType')
    include_unapproved = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='includeUnapproved')
    karma = sgqlc.types.Field(Int, graphql_name='karma')
    order = sgqlc.types.Field(OrderEnum, graphql_name='order')
    orderby = sgqlc.types.Field(CommentsConnectionOrderbyEnum, graphql_name='orderby')
    parent = sgqlc.types.Field(Int, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    search = sgqlc.types.Field(String, graphql_name='search')
    status = sgqlc.types.Field(String, graphql_name='status')
    user_id = sgqlc.types.Field(ID, graphql_name='userId')


class RootQueryToContentNodeConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('content_types', 'date_query', 'has_password', 'id', 'in_', 'mime_type', 'name', 'name_in', 'not_in', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'password', 'search', 'stati', 'status', 'title')
    content_types = sgqlc.types.Field(sgqlc.types.list_of(ContentTypeEnum), graphql_name='contentTypes')
    date_query = sgqlc.types.Field(DateQueryInput, graphql_name='dateQuery')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    id = sgqlc.types.Field(Int, graphql_name='id')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')
    mime_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='mimeType')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nameIn')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='notIn')
    orderby = sgqlc.types.Field(sgqlc.types.list_of(PostObjectsConnectionOrderbyInput), graphql_name='orderby')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    password = sgqlc.types.Field(String, graphql_name='password')
    search = sgqlc.types.Field(String, graphql_name='search')
    stati = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='stati')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class RootQueryToContractKindConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('cache_domain', 'child_of', 'childless', 'description_like', 'exclude', 'exclude_tree', 'hide_empty', 'hierarchical', 'include', 'name', 'name_like', 'object_ids', 'order', 'orderby', 'pad_counts', 'parent', 'search', 'slug', 'term_taxonom_id', 'term_taxonomy_id', 'update_term_meta_cache')
    cache_domain = sgqlc.types.Field(String, graphql_name='cacheDomain')
    child_of = sgqlc.types.Field(Int, graphql_name='childOf')
    childless = sgqlc.types.Field(Boolean, graphql_name='childless')
    description_like = sgqlc.types.Field(String, graphql_name='descriptionLike')
    exclude = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='exclude')
    exclude_tree = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='excludeTree')
    hide_empty = sgqlc.types.Field(Boolean, graphql_name='hideEmpty')
    hierarchical = sgqlc.types.Field(Boolean, graphql_name='hierarchical')
    include = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='include')
    name = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='name')
    name_like = sgqlc.types.Field(String, graphql_name='nameLike')
    object_ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='objectIds')
    order = sgqlc.types.Field(OrderEnum, graphql_name='order')
    orderby = sgqlc.types.Field(TermObjectsConnectionOrderbyEnum, graphql_name='orderby')
    pad_counts = sgqlc.types.Field(Boolean, graphql_name='padCounts')
    parent = sgqlc.types.Field(Int, graphql_name='parent')
    search = sgqlc.types.Field(String, graphql_name='search')
    slug = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='slug')
    term_taxonom_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomId')
    term_taxonomy_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomyId')
    update_term_meta_cache = sgqlc.types.Field(Boolean, graphql_name='updateTermMetaCache')


class RootQueryToEventConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author', 'author_in', 'author_name', 'author_not_in', 'date_query', 'end_date_query', 'has_password', 'id', 'in_', 'mime_type', 'name', 'name_in', 'not_in', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'password', 'search', 'start_date_query', 'stati', 'status', 'tag', 'tag_id', 'tag_in', 'tag_not_in', 'tag_slug_and', 'tag_slug_in', 'title', 'venues_in', 'venues_not_in')
    author = sgqlc.types.Field(Int, graphql_name='author')
    author_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorIn')
    author_name = sgqlc.types.Field(String, graphql_name='authorName')
    author_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorNotIn')
    date_query = sgqlc.types.Field(DateQueryInput, graphql_name='dateQuery')
    end_date_query = sgqlc.types.Field(DateQueryInput, graphql_name='endDateQuery')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    id = sgqlc.types.Field(Int, graphql_name='id')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')
    mime_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='mimeType')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nameIn')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='notIn')
    orderby = sgqlc.types.Field(sgqlc.types.list_of(PostObjectsConnectionOrderbyInput), graphql_name='orderby')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    password = sgqlc.types.Field(String, graphql_name='password')
    search = sgqlc.types.Field(String, graphql_name='search')
    start_date_query = sgqlc.types.Field(DateQueryInput, graphql_name='startDateQuery')
    stati = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='stati')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    tag = sgqlc.types.Field(String, graphql_name='tag')
    tag_id = sgqlc.types.Field(String, graphql_name='tagId')
    tag_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='tagIn')
    tag_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='tagNotIn')
    tag_slug_and = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tagSlugAnd')
    tag_slug_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tagSlugIn')
    title = sgqlc.types.Field(String, graphql_name='title')
    venues_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='venuesIn')
    venues_not_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='venuesNotIn')


class RootQueryToEventsCategoryConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('cache_domain', 'child_of', 'childless', 'description_like', 'exclude', 'exclude_tree', 'hide_empty', 'hierarchical', 'include', 'name', 'name_like', 'object_ids', 'order', 'orderby', 'pad_counts', 'parent', 'search', 'slug', 'term_taxonom_id', 'term_taxonomy_id', 'update_term_meta_cache')
    cache_domain = sgqlc.types.Field(String, graphql_name='cacheDomain')
    child_of = sgqlc.types.Field(Int, graphql_name='childOf')
    childless = sgqlc.types.Field(Boolean, graphql_name='childless')
    description_like = sgqlc.types.Field(String, graphql_name='descriptionLike')
    exclude = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='exclude')
    exclude_tree = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='excludeTree')
    hide_empty = sgqlc.types.Field(Boolean, graphql_name='hideEmpty')
    hierarchical = sgqlc.types.Field(Boolean, graphql_name='hierarchical')
    include = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='include')
    name = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='name')
    name_like = sgqlc.types.Field(String, graphql_name='nameLike')
    object_ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='objectIds')
    order = sgqlc.types.Field(OrderEnum, graphql_name='order')
    orderby = sgqlc.types.Field(TermObjectsConnectionOrderbyEnum, graphql_name='orderby')
    pad_counts = sgqlc.types.Field(Boolean, graphql_name='padCounts')
    parent = sgqlc.types.Field(Int, graphql_name='parent')
    search = sgqlc.types.Field(String, graphql_name='search')
    slug = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='slug')
    term_taxonom_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomId')
    term_taxonomy_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomyId')
    update_term_meta_cache = sgqlc.types.Field(Boolean, graphql_name='updateTermMetaCache')


class RootQueryToGraphqlDocumentConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('date_query', 'has_password', 'id', 'in_', 'mime_type', 'name', 'name_in', 'not_in', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'password', 'search', 'stati', 'status', 'title')
    date_query = sgqlc.types.Field(DateQueryInput, graphql_name='dateQuery')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    id = sgqlc.types.Field(Int, graphql_name='id')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')
    mime_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='mimeType')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nameIn')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='notIn')
    orderby = sgqlc.types.Field(sgqlc.types.list_of(PostObjectsConnectionOrderbyInput), graphql_name='orderby')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    password = sgqlc.types.Field(String, graphql_name='password')
    search = sgqlc.types.Field(String, graphql_name='search')
    stati = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='stati')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class RootQueryToGraphqlDocumentGroupConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('cache_domain', 'child_of', 'childless', 'description_like', 'exclude', 'exclude_tree', 'hide_empty', 'hierarchical', 'include', 'name', 'name_like', 'object_ids', 'order', 'orderby', 'pad_counts', 'parent', 'search', 'slug', 'term_taxonom_id', 'term_taxonomy_id', 'update_term_meta_cache')
    cache_domain = sgqlc.types.Field(String, graphql_name='cacheDomain')
    child_of = sgqlc.types.Field(Int, graphql_name='childOf')
    childless = sgqlc.types.Field(Boolean, graphql_name='childless')
    description_like = sgqlc.types.Field(String, graphql_name='descriptionLike')
    exclude = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='exclude')
    exclude_tree = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='excludeTree')
    hide_empty = sgqlc.types.Field(Boolean, graphql_name='hideEmpty')
    hierarchical = sgqlc.types.Field(Boolean, graphql_name='hierarchical')
    include = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='include')
    name = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='name')
    name_like = sgqlc.types.Field(String, graphql_name='nameLike')
    object_ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='objectIds')
    order = sgqlc.types.Field(OrderEnum, graphql_name='order')
    orderby = sgqlc.types.Field(TermObjectsConnectionOrderbyEnum, graphql_name='orderby')
    pad_counts = sgqlc.types.Field(Boolean, graphql_name='padCounts')
    parent = sgqlc.types.Field(Int, graphql_name='parent')
    search = sgqlc.types.Field(String, graphql_name='search')
    slug = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='slug')
    term_taxonom_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomId')
    term_taxonomy_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomyId')
    update_term_meta_cache = sgqlc.types.Field(Boolean, graphql_name='updateTermMetaCache')


class RootQueryToJobConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author', 'author_in', 'author_name', 'author_not_in', 'date_query', 'has_password', 'id', 'in_', 'mime_type', 'name', 'name_in', 'not_in', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'password', 'search', 'stati', 'status', 'title')
    author = sgqlc.types.Field(Int, graphql_name='author')
    author_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorIn')
    author_name = sgqlc.types.Field(String, graphql_name='authorName')
    author_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorNotIn')
    date_query = sgqlc.types.Field(DateQueryInput, graphql_name='dateQuery')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    id = sgqlc.types.Field(Int, graphql_name='id')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')
    mime_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='mimeType')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nameIn')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='notIn')
    orderby = sgqlc.types.Field(sgqlc.types.list_of(PostObjectsConnectionOrderbyInput), graphql_name='orderby')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    password = sgqlc.types.Field(String, graphql_name='password')
    search = sgqlc.types.Field(String, graphql_name='search')
    stati = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='stati')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class RootQueryToJobmodeConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('cache_domain', 'child_of', 'childless', 'description_like', 'exclude', 'exclude_tree', 'hide_empty', 'hierarchical', 'include', 'name', 'name_like', 'object_ids', 'order', 'orderby', 'pad_counts', 'parent', 'search', 'slug', 'term_taxonom_id', 'term_taxonomy_id', 'update_term_meta_cache')
    cache_domain = sgqlc.types.Field(String, graphql_name='cacheDomain')
    child_of = sgqlc.types.Field(Int, graphql_name='childOf')
    childless = sgqlc.types.Field(Boolean, graphql_name='childless')
    description_like = sgqlc.types.Field(String, graphql_name='descriptionLike')
    exclude = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='exclude')
    exclude_tree = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='excludeTree')
    hide_empty = sgqlc.types.Field(Boolean, graphql_name='hideEmpty')
    hierarchical = sgqlc.types.Field(Boolean, graphql_name='hierarchical')
    include = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='include')
    name = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='name')
    name_like = sgqlc.types.Field(String, graphql_name='nameLike')
    object_ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='objectIds')
    order = sgqlc.types.Field(OrderEnum, graphql_name='order')
    orderby = sgqlc.types.Field(TermObjectsConnectionOrderbyEnum, graphql_name='orderby')
    pad_counts = sgqlc.types.Field(Boolean, graphql_name='padCounts')
    parent = sgqlc.types.Field(Int, graphql_name='parent')
    search = sgqlc.types.Field(String, graphql_name='search')
    slug = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='slug')
    term_taxonom_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomId')
    term_taxonomy_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomyId')
    update_term_meta_cache = sgqlc.types.Field(Boolean, graphql_name='updateTermMetaCache')


class RootQueryToMediaItemConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author', 'author_in', 'author_name', 'author_not_in', 'date_query', 'has_password', 'id', 'in_', 'mime_type', 'name', 'name_in', 'not_in', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'password', 'search', 'stati', 'status', 'title')
    author = sgqlc.types.Field(Int, graphql_name='author')
    author_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorIn')
    author_name = sgqlc.types.Field(String, graphql_name='authorName')
    author_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorNotIn')
    date_query = sgqlc.types.Field(DateQueryInput, graphql_name='dateQuery')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    id = sgqlc.types.Field(Int, graphql_name='id')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')
    mime_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='mimeType')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nameIn')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='notIn')
    orderby = sgqlc.types.Field(sgqlc.types.list_of(PostObjectsConnectionOrderbyInput), graphql_name='orderby')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    password = sgqlc.types.Field(String, graphql_name='password')
    search = sgqlc.types.Field(String, graphql_name='search')
    stati = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='stati')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class RootQueryToMenuConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'location', 'slug')
    id = sgqlc.types.Field(Int, graphql_name='id')
    location = sgqlc.types.Field(MenuLocationEnum, graphql_name='location')
    slug = sgqlc.types.Field(String, graphql_name='slug')


class RootQueryToMenuItemConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'location', 'parent_database_id', 'parent_id')
    id = sgqlc.types.Field(Int, graphql_name='id')
    location = sgqlc.types.Field(MenuLocationEnum, graphql_name='location')
    parent_database_id = sgqlc.types.Field(Int, graphql_name='parentDatabaseId')
    parent_id = sgqlc.types.Field(ID, graphql_name='parentId')


class RootQueryToOccupationkindConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('cache_domain', 'child_of', 'childless', 'description_like', 'exclude', 'exclude_tree', 'hide_empty', 'hierarchical', 'include', 'name', 'name_like', 'object_ids', 'order', 'orderby', 'pad_counts', 'parent', 'search', 'slug', 'term_taxonom_id', 'term_taxonomy_id', 'update_term_meta_cache')
    cache_domain = sgqlc.types.Field(String, graphql_name='cacheDomain')
    child_of = sgqlc.types.Field(Int, graphql_name='childOf')
    childless = sgqlc.types.Field(Boolean, graphql_name='childless')
    description_like = sgqlc.types.Field(String, graphql_name='descriptionLike')
    exclude = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='exclude')
    exclude_tree = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='excludeTree')
    hide_empty = sgqlc.types.Field(Boolean, graphql_name='hideEmpty')
    hierarchical = sgqlc.types.Field(Boolean, graphql_name='hierarchical')
    include = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='include')
    name = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='name')
    name_like = sgqlc.types.Field(String, graphql_name='nameLike')
    object_ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='objectIds')
    order = sgqlc.types.Field(OrderEnum, graphql_name='order')
    orderby = sgqlc.types.Field(TermObjectsConnectionOrderbyEnum, graphql_name='orderby')
    pad_counts = sgqlc.types.Field(Boolean, graphql_name='padCounts')
    parent = sgqlc.types.Field(Int, graphql_name='parent')
    search = sgqlc.types.Field(String, graphql_name='search')
    slug = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='slug')
    term_taxonom_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomId')
    term_taxonomy_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomyId')
    update_term_meta_cache = sgqlc.types.Field(Boolean, graphql_name='updateTermMetaCache')


class RootQueryToOrganizerConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author', 'author_in', 'author_name', 'author_not_in', 'date_query', 'has_password', 'id', 'in_', 'mime_type', 'name', 'name_in', 'not_in', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'password', 'search', 'stati', 'status', 'title')
    author = sgqlc.types.Field(Int, graphql_name='author')
    author_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorIn')
    author_name = sgqlc.types.Field(String, graphql_name='authorName')
    author_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorNotIn')
    date_query = sgqlc.types.Field(DateQueryInput, graphql_name='dateQuery')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    id = sgqlc.types.Field(Int, graphql_name='id')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')
    mime_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='mimeType')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nameIn')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='notIn')
    orderby = sgqlc.types.Field(sgqlc.types.list_of(PostObjectsConnectionOrderbyInput), graphql_name='orderby')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    password = sgqlc.types.Field(String, graphql_name='password')
    search = sgqlc.types.Field(String, graphql_name='search')
    stati = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='stati')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class RootQueryToPageConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author', 'author_in', 'author_name', 'author_not_in', 'date_query', 'has_password', 'id', 'in_', 'mime_type', 'name', 'name_in', 'not_in', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'password', 'search', 'stati', 'status', 'title')
    author = sgqlc.types.Field(Int, graphql_name='author')
    author_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorIn')
    author_name = sgqlc.types.Field(String, graphql_name='authorName')
    author_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorNotIn')
    date_query = sgqlc.types.Field(DateQueryInput, graphql_name='dateQuery')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    id = sgqlc.types.Field(Int, graphql_name='id')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')
    mime_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='mimeType')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nameIn')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='notIn')
    orderby = sgqlc.types.Field(sgqlc.types.list_of(PostObjectsConnectionOrderbyInput), graphql_name='orderby')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    password = sgqlc.types.Field(String, graphql_name='password')
    search = sgqlc.types.Field(String, graphql_name='search')
    stati = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='stati')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class RootQueryToPartnerConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author', 'author_in', 'author_name', 'author_not_in', 'date_query', 'has_password', 'id', 'in_', 'mime_type', 'name', 'name_in', 'not_in', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'password', 'search', 'stati', 'status', 'title')
    author = sgqlc.types.Field(Int, graphql_name='author')
    author_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorIn')
    author_name = sgqlc.types.Field(String, graphql_name='authorName')
    author_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorNotIn')
    date_query = sgqlc.types.Field(DateQueryInput, graphql_name='dateQuery')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    id = sgqlc.types.Field(Int, graphql_name='id')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')
    mime_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='mimeType')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nameIn')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='notIn')
    orderby = sgqlc.types.Field(sgqlc.types.list_of(PostObjectsConnectionOrderbyInput), graphql_name='orderby')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    password = sgqlc.types.Field(String, graphql_name='password')
    search = sgqlc.types.Field(String, graphql_name='search')
    stati = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='stati')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class RootQueryToPluginConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('search', 'stati', 'status')
    search = sgqlc.types.Field(String, graphql_name='search')
    stati = sgqlc.types.Field(sgqlc.types.list_of(PluginStatusEnum), graphql_name='stati')
    status = sgqlc.types.Field(PluginStatusEnum, graphql_name='status')


class RootQueryToPostConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author', 'author_in', 'author_name', 'author_not_in', 'category_id', 'category_in', 'category_name', 'category_not_in', 'date_query', 'has_password', 'id', 'in_', 'mime_type', 'name', 'name_in', 'not_in', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'password', 'search', 'stati', 'status', 'tag', 'tag_id', 'tag_in', 'tag_not_in', 'tag_slug_and', 'tag_slug_in', 'title')
    author = sgqlc.types.Field(Int, graphql_name='author')
    author_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorIn')
    author_name = sgqlc.types.Field(String, graphql_name='authorName')
    author_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorNotIn')
    category_id = sgqlc.types.Field(Int, graphql_name='categoryId')
    category_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='categoryIn')
    category_name = sgqlc.types.Field(String, graphql_name='categoryName')
    category_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='categoryNotIn')
    date_query = sgqlc.types.Field(DateQueryInput, graphql_name='dateQuery')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    id = sgqlc.types.Field(Int, graphql_name='id')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')
    mime_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='mimeType')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nameIn')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='notIn')
    orderby = sgqlc.types.Field(sgqlc.types.list_of(PostObjectsConnectionOrderbyInput), graphql_name='orderby')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    password = sgqlc.types.Field(String, graphql_name='password')
    search = sgqlc.types.Field(String, graphql_name='search')
    stati = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='stati')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    tag = sgqlc.types.Field(String, graphql_name='tag')
    tag_id = sgqlc.types.Field(String, graphql_name='tagId')
    tag_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='tagIn')
    tag_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='tagNotIn')
    tag_slug_and = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tagSlugAnd')
    tag_slug_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tagSlugIn')
    title = sgqlc.types.Field(String, graphql_name='title')


class RootQueryToPostFormatConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('cache_domain', 'child_of', 'childless', 'description_like', 'exclude', 'exclude_tree', 'hide_empty', 'hierarchical', 'include', 'name', 'name_like', 'object_ids', 'order', 'orderby', 'pad_counts', 'parent', 'search', 'slug', 'term_taxonom_id', 'term_taxonomy_id', 'update_term_meta_cache')
    cache_domain = sgqlc.types.Field(String, graphql_name='cacheDomain')
    child_of = sgqlc.types.Field(Int, graphql_name='childOf')
    childless = sgqlc.types.Field(Boolean, graphql_name='childless')
    description_like = sgqlc.types.Field(String, graphql_name='descriptionLike')
    exclude = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='exclude')
    exclude_tree = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='excludeTree')
    hide_empty = sgqlc.types.Field(Boolean, graphql_name='hideEmpty')
    hierarchical = sgqlc.types.Field(Boolean, graphql_name='hierarchical')
    include = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='include')
    name = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='name')
    name_like = sgqlc.types.Field(String, graphql_name='nameLike')
    object_ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='objectIds')
    order = sgqlc.types.Field(OrderEnum, graphql_name='order')
    orderby = sgqlc.types.Field(TermObjectsConnectionOrderbyEnum, graphql_name='orderby')
    pad_counts = sgqlc.types.Field(Boolean, graphql_name='padCounts')
    parent = sgqlc.types.Field(Int, graphql_name='parent')
    search = sgqlc.types.Field(String, graphql_name='search')
    slug = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='slug')
    term_taxonom_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomId')
    term_taxonomy_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomyId')
    update_term_meta_cache = sgqlc.types.Field(Boolean, graphql_name='updateTermMetaCache')


class RootQueryToRevisionsConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('content_types', 'date_query', 'has_password', 'id', 'in_', 'mime_type', 'name', 'name_in', 'not_in', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'password', 'search', 'stati', 'status', 'title')
    content_types = sgqlc.types.Field(sgqlc.types.list_of(ContentTypeEnum), graphql_name='contentTypes')
    date_query = sgqlc.types.Field(DateQueryInput, graphql_name='dateQuery')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    id = sgqlc.types.Field(Int, graphql_name='id')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')
    mime_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='mimeType')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nameIn')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='notIn')
    orderby = sgqlc.types.Field(sgqlc.types.list_of(PostObjectsConnectionOrderbyInput), graphql_name='orderby')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    password = sgqlc.types.Field(String, graphql_name='password')
    search = sgqlc.types.Field(String, graphql_name='search')
    stati = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='stati')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class RootQueryToTagConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('cache_domain', 'child_of', 'childless', 'description_like', 'exclude', 'exclude_tree', 'hide_empty', 'hierarchical', 'include', 'name', 'name_like', 'object_ids', 'order', 'orderby', 'pad_counts', 'parent', 'search', 'slug', 'term_taxonom_id', 'term_taxonomy_id', 'update_term_meta_cache')
    cache_domain = sgqlc.types.Field(String, graphql_name='cacheDomain')
    child_of = sgqlc.types.Field(Int, graphql_name='childOf')
    childless = sgqlc.types.Field(Boolean, graphql_name='childless')
    description_like = sgqlc.types.Field(String, graphql_name='descriptionLike')
    exclude = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='exclude')
    exclude_tree = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='excludeTree')
    hide_empty = sgqlc.types.Field(Boolean, graphql_name='hideEmpty')
    hierarchical = sgqlc.types.Field(Boolean, graphql_name='hierarchical')
    include = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='include')
    name = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='name')
    name_like = sgqlc.types.Field(String, graphql_name='nameLike')
    object_ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='objectIds')
    order = sgqlc.types.Field(OrderEnum, graphql_name='order')
    orderby = sgqlc.types.Field(TermObjectsConnectionOrderbyEnum, graphql_name='orderby')
    pad_counts = sgqlc.types.Field(Boolean, graphql_name='padCounts')
    parent = sgqlc.types.Field(Int, graphql_name='parent')
    search = sgqlc.types.Field(String, graphql_name='search')
    slug = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='slug')
    term_taxonom_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomId')
    term_taxonomy_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomyId')
    update_term_meta_cache = sgqlc.types.Field(Boolean, graphql_name='updateTermMetaCache')


class RootQueryToTermNodeConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('cache_domain', 'child_of', 'childless', 'description_like', 'exclude', 'exclude_tree', 'hide_empty', 'hierarchical', 'include', 'name', 'name_like', 'object_ids', 'order', 'orderby', 'pad_counts', 'parent', 'search', 'slug', 'taxonomies', 'term_taxonom_id', 'term_taxonomy_id', 'update_term_meta_cache')
    cache_domain = sgqlc.types.Field(String, graphql_name='cacheDomain')
    child_of = sgqlc.types.Field(Int, graphql_name='childOf')
    childless = sgqlc.types.Field(Boolean, graphql_name='childless')
    description_like = sgqlc.types.Field(String, graphql_name='descriptionLike')
    exclude = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='exclude')
    exclude_tree = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='excludeTree')
    hide_empty = sgqlc.types.Field(Boolean, graphql_name='hideEmpty')
    hierarchical = sgqlc.types.Field(Boolean, graphql_name='hierarchical')
    include = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='include')
    name = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='name')
    name_like = sgqlc.types.Field(String, graphql_name='nameLike')
    object_ids = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='objectIds')
    order = sgqlc.types.Field(OrderEnum, graphql_name='order')
    orderby = sgqlc.types.Field(TermObjectsConnectionOrderbyEnum, graphql_name='orderby')
    pad_counts = sgqlc.types.Field(Boolean, graphql_name='padCounts')
    parent = sgqlc.types.Field(Int, graphql_name='parent')
    search = sgqlc.types.Field(String, graphql_name='search')
    slug = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='slug')
    taxonomies = sgqlc.types.Field(sgqlc.types.list_of(TaxonomyEnum), graphql_name='taxonomies')
    term_taxonom_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomId')
    term_taxonomy_id = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='termTaxonomyId')
    update_term_meta_cache = sgqlc.types.Field(Boolean, graphql_name='updateTermMetaCache')


class RootQueryToUserConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('exclude', 'has_published_posts', 'include', 'login', 'login_in', 'login_not_in', 'nicename', 'nicename_in', 'nicename_not_in', 'orderby', 'role', 'role_in', 'role_not_in', 'search', 'search_columns')
    exclude = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='exclude')
    has_published_posts = sgqlc.types.Field(sgqlc.types.list_of(ContentTypeEnum), graphql_name='hasPublishedPosts')
    include = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='include')
    login = sgqlc.types.Field(String, graphql_name='login')
    login_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='loginIn')
    login_not_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='loginNotIn')
    nicename = sgqlc.types.Field(String, graphql_name='nicename')
    nicename_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nicenameIn')
    nicename_not_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nicenameNotIn')
    orderby = sgqlc.types.Field(sgqlc.types.list_of('UsersConnectionOrderbyInput'), graphql_name='orderby')
    role = sgqlc.types.Field(UserRoleEnum, graphql_name='role')
    role_in = sgqlc.types.Field(sgqlc.types.list_of(UserRoleEnum), graphql_name='roleIn')
    role_not_in = sgqlc.types.Field(sgqlc.types.list_of(UserRoleEnum), graphql_name='roleNotIn')
    search = sgqlc.types.Field(String, graphql_name='search')
    search_columns = sgqlc.types.Field(sgqlc.types.list_of(UsersConnectionSearchColumnEnum), graphql_name='searchColumns')


class RootQueryToVenueConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author', 'author_in', 'author_name', 'author_not_in', 'date_query', 'has_password', 'id', 'in_', 'mime_type', 'name', 'name_in', 'not_in', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'password', 'search', 'stati', 'status', 'title')
    author = sgqlc.types.Field(Int, graphql_name='author')
    author_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorIn')
    author_name = sgqlc.types.Field(String, graphql_name='authorName')
    author_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorNotIn')
    date_query = sgqlc.types.Field(DateQueryInput, graphql_name='dateQuery')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    id = sgqlc.types.Field(Int, graphql_name='id')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')
    mime_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='mimeType')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nameIn')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='notIn')
    orderby = sgqlc.types.Field(sgqlc.types.list_of(PostObjectsConnectionOrderbyInput), graphql_name='orderby')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    password = sgqlc.types.Field(String, graphql_name='password')
    search = sgqlc.types.Field(String, graphql_name='search')
    stati = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='stati')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class SendPasswordResetEmailInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'username')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    username = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='username')


class TagToContentNodeConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('content_types', 'date_query', 'has_password', 'id', 'in_', 'mime_type', 'name', 'name_in', 'not_in', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'password', 'search', 'stati', 'status', 'title')
    content_types = sgqlc.types.Field(sgqlc.types.list_of(ContentTypesOfTagEnum), graphql_name='contentTypes')
    date_query = sgqlc.types.Field(DateQueryInput, graphql_name='dateQuery')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    id = sgqlc.types.Field(Int, graphql_name='id')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')
    mime_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='mimeType')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nameIn')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='notIn')
    orderby = sgqlc.types.Field(sgqlc.types.list_of(PostObjectsConnectionOrderbyInput), graphql_name='orderby')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    password = sgqlc.types.Field(String, graphql_name='password')
    search = sgqlc.types.Field(String, graphql_name='search')
    stati = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='stati')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class TagToEventConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author', 'author_in', 'author_name', 'author_not_in', 'date_query', 'end_date_query', 'has_password', 'id', 'in_', 'mime_type', 'name', 'name_in', 'not_in', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'password', 'search', 'start_date_query', 'stati', 'status', 'tag', 'tag_id', 'tag_in', 'tag_not_in', 'tag_slug_and', 'tag_slug_in', 'title', 'venues_in', 'venues_not_in')
    author = sgqlc.types.Field(Int, graphql_name='author')
    author_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorIn')
    author_name = sgqlc.types.Field(String, graphql_name='authorName')
    author_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorNotIn')
    date_query = sgqlc.types.Field(DateQueryInput, graphql_name='dateQuery')
    end_date_query = sgqlc.types.Field(DateQueryInput, graphql_name='endDateQuery')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    id = sgqlc.types.Field(Int, graphql_name='id')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')
    mime_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='mimeType')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nameIn')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='notIn')
    orderby = sgqlc.types.Field(sgqlc.types.list_of(PostObjectsConnectionOrderbyInput), graphql_name='orderby')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    password = sgqlc.types.Field(String, graphql_name='password')
    search = sgqlc.types.Field(String, graphql_name='search')
    start_date_query = sgqlc.types.Field(DateQueryInput, graphql_name='startDateQuery')
    stati = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='stati')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    tag = sgqlc.types.Field(String, graphql_name='tag')
    tag_id = sgqlc.types.Field(String, graphql_name='tagId')
    tag_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='tagIn')
    tag_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='tagNotIn')
    tag_slug_and = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tagSlugAnd')
    tag_slug_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tagSlugIn')
    title = sgqlc.types.Field(String, graphql_name='title')
    venues_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='venuesIn')
    venues_not_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='venuesNotIn')


class TagToPostConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author', 'author_in', 'author_name', 'author_not_in', 'category_id', 'category_in', 'category_name', 'category_not_in', 'date_query', 'has_password', 'id', 'in_', 'mime_type', 'name', 'name_in', 'not_in', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'password', 'search', 'stati', 'status', 'tag', 'tag_id', 'tag_in', 'tag_not_in', 'tag_slug_and', 'tag_slug_in', 'title')
    author = sgqlc.types.Field(Int, graphql_name='author')
    author_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorIn')
    author_name = sgqlc.types.Field(String, graphql_name='authorName')
    author_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorNotIn')
    category_id = sgqlc.types.Field(Int, graphql_name='categoryId')
    category_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='categoryIn')
    category_name = sgqlc.types.Field(String, graphql_name='categoryName')
    category_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='categoryNotIn')
    date_query = sgqlc.types.Field(DateQueryInput, graphql_name='dateQuery')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    id = sgqlc.types.Field(Int, graphql_name='id')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')
    mime_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='mimeType')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nameIn')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='notIn')
    orderby = sgqlc.types.Field(sgqlc.types.list_of(PostObjectsConnectionOrderbyInput), graphql_name='orderby')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    password = sgqlc.types.Field(String, graphql_name='password')
    search = sgqlc.types.Field(String, graphql_name='search')
    stati = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='stati')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    tag = sgqlc.types.Field(String, graphql_name='tag')
    tag_id = sgqlc.types.Field(String, graphql_name='tagId')
    tag_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='tagIn')
    tag_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='tagNotIn')
    tag_slug_and = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tagSlugAnd')
    tag_slug_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tagSlugIn')
    title = sgqlc.types.Field(String, graphql_name='title')


class UpdateCategoryInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('alias_of', 'client_mutation_id', 'description', 'id', 'name', 'parent_id', 'slug')
    alias_of = sgqlc.types.Field(String, graphql_name='aliasOf')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    description = sgqlc.types.Field(String, graphql_name='description')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    parent_id = sgqlc.types.Field(ID, graphql_name='parentId')
    slug = sgqlc.types.Field(String, graphql_name='slug')


class UpdateCommentInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('approved', 'author', 'author_email', 'author_url', 'client_mutation_id', 'comment_on', 'content', 'date', 'id', 'parent', 'status', 'type')
    approved = sgqlc.types.Field(String, graphql_name='approved')
    author = sgqlc.types.Field(String, graphql_name='author')
    author_email = sgqlc.types.Field(String, graphql_name='authorEmail')
    author_url = sgqlc.types.Field(String, graphql_name='authorUrl')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    comment_on = sgqlc.types.Field(Int, graphql_name='commentOn')
    content = sgqlc.types.Field(String, graphql_name='content')
    date = sgqlc.types.Field(String, graphql_name='date')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    status = sgqlc.types.Field(CommentStatusEnum, graphql_name='status')
    type = sgqlc.types.Field(String, graphql_name='type')


class UpdateContractKindInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('alias_of', 'client_mutation_id', 'description', 'id', 'name', 'parent_id', 'slug')
    alias_of = sgqlc.types.Field(String, graphql_name='aliasOf')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    description = sgqlc.types.Field(String, graphql_name='description')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    parent_id = sgqlc.types.Field(ID, graphql_name='parentId')
    slug = sgqlc.types.Field(String, graphql_name='slug')


class UpdateEventInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('events_categories', 'author_id', 'client_mutation_id', 'comment_status', 'content', 'date', 'excerpt', 'id', 'ignore_edit_lock', 'menu_order', 'password', 'slug', 'status', 'tags', 'title')
    events_categories = sgqlc.types.Field(EventEventsCategoriesInput, graphql_name='eventsCategories')
    author_id = sgqlc.types.Field(ID, graphql_name='authorId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    comment_status = sgqlc.types.Field(String, graphql_name='commentStatus')
    content = sgqlc.types.Field(String, graphql_name='content')
    date = sgqlc.types.Field(String, graphql_name='date')
    excerpt = sgqlc.types.Field(String, graphql_name='excerpt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    ignore_edit_lock = sgqlc.types.Field(Boolean, graphql_name='ignoreEditLock')
    menu_order = sgqlc.types.Field(Int, graphql_name='menuOrder')
    password = sgqlc.types.Field(String, graphql_name='password')
    slug = sgqlc.types.Field(String, graphql_name='slug')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    tags = sgqlc.types.Field(EventTagsInput, graphql_name='tags')
    title = sgqlc.types.Field(String, graphql_name='title')


class UpdateEventsCategoryInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('alias_of', 'client_mutation_id', 'description', 'id', 'name', 'parent_id', 'slug')
    alias_of = sgqlc.types.Field(String, graphql_name='aliasOf')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    description = sgqlc.types.Field(String, graphql_name='description')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    parent_id = sgqlc.types.Field(ID, graphql_name='parentId')
    slug = sgqlc.types.Field(String, graphql_name='slug')


class UpdateGraphqlDocumentGroupInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('alias_of', 'client_mutation_id', 'description', 'id', 'name', 'slug')
    alias_of = sgqlc.types.Field(String, graphql_name='aliasOf')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    description = sgqlc.types.Field(String, graphql_name='description')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    slug = sgqlc.types.Field(String, graphql_name='slug')


class UpdateGraphqlDocumentInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('alias', 'client_mutation_id', 'content', 'date', 'description', 'grant', 'graphql_document_groups', 'id', 'ignore_edit_lock', 'max_age_header', 'menu_order', 'password', 'slug', 'status', 'title')
    alias = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='alias')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    content = sgqlc.types.Field(String, graphql_name='content')
    date = sgqlc.types.Field(String, graphql_name='date')
    description = sgqlc.types.Field(String, graphql_name='description')
    grant = sgqlc.types.Field(String, graphql_name='grant')
    graphql_document_groups = sgqlc.types.Field(GraphqlDocumentGraphqlDocumentGroupsInput, graphql_name='graphqlDocumentGroups')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    ignore_edit_lock = sgqlc.types.Field(Boolean, graphql_name='ignoreEditLock')
    max_age_header = sgqlc.types.Field(Int, graphql_name='maxAgeHeader')
    menu_order = sgqlc.types.Field(Int, graphql_name='menuOrder')
    password = sgqlc.types.Field(String, graphql_name='password')
    slug = sgqlc.types.Field(String, graphql_name='slug')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class UpdateJobInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author_id', 'client_mutation_id', 'contractkinds', 'date', 'id', 'ignore_edit_lock', 'jobmodes', 'menu_order', 'occupationkinds', 'password', 'slug', 'status', 'title')
    author_id = sgqlc.types.Field(ID, graphql_name='authorId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    contractkinds = sgqlc.types.Field(JobContractkindsInput, graphql_name='contractkinds')
    date = sgqlc.types.Field(String, graphql_name='date')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    ignore_edit_lock = sgqlc.types.Field(Boolean, graphql_name='ignoreEditLock')
    jobmodes = sgqlc.types.Field(JobJobmodesInput, graphql_name='jobmodes')
    menu_order = sgqlc.types.Field(Int, graphql_name='menuOrder')
    occupationkinds = sgqlc.types.Field(JobOccupationkindsInput, graphql_name='occupationkinds')
    password = sgqlc.types.Field(String, graphql_name='password')
    slug = sgqlc.types.Field(String, graphql_name='slug')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class UpdateJobmodeInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('alias_of', 'client_mutation_id', 'description', 'id', 'name', 'slug')
    alias_of = sgqlc.types.Field(String, graphql_name='aliasOf')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    description = sgqlc.types.Field(String, graphql_name='description')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    slug = sgqlc.types.Field(String, graphql_name='slug')


class UpdateMediaItemInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('alt_text', 'author_id', 'caption', 'client_mutation_id', 'comment_status', 'date', 'date_gmt', 'description', 'file_path', 'file_type', 'id', 'parent_id', 'ping_status', 'slug', 'status', 'title')
    alt_text = sgqlc.types.Field(String, graphql_name='altText')
    author_id = sgqlc.types.Field(ID, graphql_name='authorId')
    caption = sgqlc.types.Field(String, graphql_name='caption')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    comment_status = sgqlc.types.Field(String, graphql_name='commentStatus')
    date = sgqlc.types.Field(String, graphql_name='date')
    date_gmt = sgqlc.types.Field(String, graphql_name='dateGmt')
    description = sgqlc.types.Field(String, graphql_name='description')
    file_path = sgqlc.types.Field(String, graphql_name='filePath')
    file_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='fileType')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    parent_id = sgqlc.types.Field(ID, graphql_name='parentId')
    ping_status = sgqlc.types.Field(String, graphql_name='pingStatus')
    slug = sgqlc.types.Field(String, graphql_name='slug')
    status = sgqlc.types.Field(MediaItemStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class UpdateOccupationkindInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('alias_of', 'client_mutation_id', 'description', 'id', 'name', 'slug')
    alias_of = sgqlc.types.Field(String, graphql_name='aliasOf')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    description = sgqlc.types.Field(String, graphql_name='description')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    slug = sgqlc.types.Field(String, graphql_name='slug')


class UpdateOrganizerInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author_id', 'client_mutation_id', 'content', 'date', 'excerpt', 'id', 'ignore_edit_lock', 'menu_order', 'password', 'slug', 'status', 'title')
    author_id = sgqlc.types.Field(ID, graphql_name='authorId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    content = sgqlc.types.Field(String, graphql_name='content')
    date = sgqlc.types.Field(String, graphql_name='date')
    excerpt = sgqlc.types.Field(String, graphql_name='excerpt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    ignore_edit_lock = sgqlc.types.Field(Boolean, graphql_name='ignoreEditLock')
    menu_order = sgqlc.types.Field(Int, graphql_name='menuOrder')
    password = sgqlc.types.Field(String, graphql_name='password')
    slug = sgqlc.types.Field(String, graphql_name='slug')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class UpdatePageInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author_id', 'client_mutation_id', 'comment_status', 'content', 'date', 'id', 'ignore_edit_lock', 'menu_order', 'parent_id', 'password', 'slug', 'status', 'title')
    author_id = sgqlc.types.Field(ID, graphql_name='authorId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    comment_status = sgqlc.types.Field(String, graphql_name='commentStatus')
    content = sgqlc.types.Field(String, graphql_name='content')
    date = sgqlc.types.Field(String, graphql_name='date')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    ignore_edit_lock = sgqlc.types.Field(Boolean, graphql_name='ignoreEditLock')
    menu_order = sgqlc.types.Field(Int, graphql_name='menuOrder')
    parent_id = sgqlc.types.Field(ID, graphql_name='parentId')
    password = sgqlc.types.Field(String, graphql_name='password')
    slug = sgqlc.types.Field(String, graphql_name='slug')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class UpdatePartnerInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author_id', 'client_mutation_id', 'date', 'id', 'ignore_edit_lock', 'menu_order', 'password', 'slug', 'status', 'title')
    author_id = sgqlc.types.Field(ID, graphql_name='authorId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    date = sgqlc.types.Field(String, graphql_name='date')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    ignore_edit_lock = sgqlc.types.Field(Boolean, graphql_name='ignoreEditLock')
    menu_order = sgqlc.types.Field(Int, graphql_name='menuOrder')
    password = sgqlc.types.Field(String, graphql_name='password')
    slug = sgqlc.types.Field(String, graphql_name='slug')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class UpdatePostFormatInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('alias_of', 'client_mutation_id', 'description', 'id', 'name', 'slug')
    alias_of = sgqlc.types.Field(String, graphql_name='aliasOf')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    description = sgqlc.types.Field(String, graphql_name='description')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    slug = sgqlc.types.Field(String, graphql_name='slug')


class UpdatePostInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author_id', 'categories', 'client_mutation_id', 'comment_status', 'content', 'date', 'excerpt', 'id', 'ignore_edit_lock', 'menu_order', 'password', 'ping_status', 'pinged', 'post_formats', 'slug', 'status', 'tags', 'title', 'to_ping')
    author_id = sgqlc.types.Field(ID, graphql_name='authorId')
    categories = sgqlc.types.Field(PostCategoriesInput, graphql_name='categories')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    comment_status = sgqlc.types.Field(String, graphql_name='commentStatus')
    content = sgqlc.types.Field(String, graphql_name='content')
    date = sgqlc.types.Field(String, graphql_name='date')
    excerpt = sgqlc.types.Field(String, graphql_name='excerpt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    ignore_edit_lock = sgqlc.types.Field(Boolean, graphql_name='ignoreEditLock')
    menu_order = sgqlc.types.Field(Int, graphql_name='menuOrder')
    password = sgqlc.types.Field(String, graphql_name='password')
    ping_status = sgqlc.types.Field(String, graphql_name='pingStatus')
    pinged = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='pinged')
    post_formats = sgqlc.types.Field(PostPostFormatsInput, graphql_name='postFormats')
    slug = sgqlc.types.Field(String, graphql_name='slug')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    tags = sgqlc.types.Field(PostTagsInput, graphql_name='tags')
    title = sgqlc.types.Field(String, graphql_name='title')
    to_ping = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='toPing')


class UpdateSettingsInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'discussion_settings_default_comment_status', 'discussion_settings_default_ping_status', 'general_settings_date_format', 'general_settings_description', 'general_settings_email', 'general_settings_language', 'general_settings_start_of_week', 'general_settings_time_format', 'general_settings_timezone', 'general_settings_title', 'general_settings_url', 'reading_settings_page_for_posts', 'reading_settings_page_on_front', 'reading_settings_posts_per_page', 'reading_settings_show_on_front', 'writing_settings_default_category', 'writing_settings_default_post_format', 'writing_settings_use_smilies')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    discussion_settings_default_comment_status = sgqlc.types.Field(String, graphql_name='discussionSettingsDefaultCommentStatus')
    discussion_settings_default_ping_status = sgqlc.types.Field(String, graphql_name='discussionSettingsDefaultPingStatus')
    general_settings_date_format = sgqlc.types.Field(String, graphql_name='generalSettingsDateFormat')
    general_settings_description = sgqlc.types.Field(String, graphql_name='generalSettingsDescription')
    general_settings_email = sgqlc.types.Field(String, graphql_name='generalSettingsEmail')
    general_settings_language = sgqlc.types.Field(String, graphql_name='generalSettingsLanguage')
    general_settings_start_of_week = sgqlc.types.Field(Int, graphql_name='generalSettingsStartOfWeek')
    general_settings_time_format = sgqlc.types.Field(String, graphql_name='generalSettingsTimeFormat')
    general_settings_timezone = sgqlc.types.Field(String, graphql_name='generalSettingsTimezone')
    general_settings_title = sgqlc.types.Field(String, graphql_name='generalSettingsTitle')
    general_settings_url = sgqlc.types.Field(String, graphql_name='generalSettingsUrl')
    reading_settings_page_for_posts = sgqlc.types.Field(Int, graphql_name='readingSettingsPageForPosts')
    reading_settings_page_on_front = sgqlc.types.Field(Int, graphql_name='readingSettingsPageOnFront')
    reading_settings_posts_per_page = sgqlc.types.Field(Int, graphql_name='readingSettingsPostsPerPage')
    reading_settings_show_on_front = sgqlc.types.Field(String, graphql_name='readingSettingsShowOnFront')
    writing_settings_default_category = sgqlc.types.Field(Int, graphql_name='writingSettingsDefaultCategory')
    writing_settings_default_post_format = sgqlc.types.Field(String, graphql_name='writingSettingsDefaultPostFormat')
    writing_settings_use_smilies = sgqlc.types.Field(Boolean, graphql_name='writingSettingsUseSmilies')


class UpdateTagInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('alias_of', 'client_mutation_id', 'description', 'id', 'name', 'slug')
    alias_of = sgqlc.types.Field(String, graphql_name='aliasOf')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    description = sgqlc.types.Field(String, graphql_name='description')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    slug = sgqlc.types.Field(String, graphql_name='slug')


class UpdateUserInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('aim', 'client_mutation_id', 'description', 'display_name', 'email', 'first_name', 'id', 'jabber', 'last_name', 'locale', 'nicename', 'nickname', 'password', 'refresh_jwt_user_secret', 'registered', 'revoke_jwt_user_secret', 'rich_editing', 'roles', 'website_url', 'yim')
    aim = sgqlc.types.Field(String, graphql_name='aim')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    description = sgqlc.types.Field(String, graphql_name='description')
    display_name = sgqlc.types.Field(String, graphql_name='displayName')
    email = sgqlc.types.Field(String, graphql_name='email')
    first_name = sgqlc.types.Field(String, graphql_name='firstName')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    jabber = sgqlc.types.Field(String, graphql_name='jabber')
    last_name = sgqlc.types.Field(String, graphql_name='lastName')
    locale = sgqlc.types.Field(String, graphql_name='locale')
    nicename = sgqlc.types.Field(String, graphql_name='nicename')
    nickname = sgqlc.types.Field(String, graphql_name='nickname')
    password = sgqlc.types.Field(String, graphql_name='password')
    refresh_jwt_user_secret = sgqlc.types.Field(Boolean, graphql_name='refreshJwtUserSecret')
    registered = sgqlc.types.Field(String, graphql_name='registered')
    revoke_jwt_user_secret = sgqlc.types.Field(Boolean, graphql_name='revokeJwtUserSecret')
    rich_editing = sgqlc.types.Field(String, graphql_name='richEditing')
    roles = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='roles')
    website_url = sgqlc.types.Field(String, graphql_name='websiteUrl')
    yim = sgqlc.types.Field(String, graphql_name='yim')


class UpdateVenueInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author_id', 'client_mutation_id', 'content', 'date', 'excerpt', 'id', 'ignore_edit_lock', 'menu_order', 'password', 'slug', 'status', 'title')
    author_id = sgqlc.types.Field(ID, graphql_name='authorId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    content = sgqlc.types.Field(String, graphql_name='content')
    date = sgqlc.types.Field(String, graphql_name='date')
    excerpt = sgqlc.types.Field(String, graphql_name='excerpt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    ignore_edit_lock = sgqlc.types.Field(Boolean, graphql_name='ignoreEditLock')
    menu_order = sgqlc.types.Field(Int, graphql_name='menuOrder')
    password = sgqlc.types.Field(String, graphql_name='password')
    slug = sgqlc.types.Field(String, graphql_name='slug')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class UserToCommentConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author_email', 'author_in', 'author_not_in', 'author_url', 'comment_in', 'comment_not_in', 'comment_type', 'comment_type_in', 'comment_type_not_in', 'content_author', 'content_author_in', 'content_author_not_in', 'content_id', 'content_id_in', 'content_id_not_in', 'content_name', 'content_parent', 'content_status', 'content_type', 'include_unapproved', 'karma', 'order', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'search', 'status', 'user_id')
    author_email = sgqlc.types.Field(String, graphql_name='authorEmail')
    author_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorIn')
    author_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorNotIn')
    author_url = sgqlc.types.Field(String, graphql_name='authorUrl')
    comment_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='commentIn')
    comment_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='commentNotIn')
    comment_type = sgqlc.types.Field(String, graphql_name='commentType')
    comment_type_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='commentTypeIn')
    comment_type_not_in = sgqlc.types.Field(String, graphql_name='commentTypeNotIn')
    content_author = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='contentAuthor')
    content_author_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='contentAuthorIn')
    content_author_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='contentAuthorNotIn')
    content_id = sgqlc.types.Field(ID, graphql_name='contentId')
    content_id_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='contentIdIn')
    content_id_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='contentIdNotIn')
    content_name = sgqlc.types.Field(String, graphql_name='contentName')
    content_parent = sgqlc.types.Field(Int, graphql_name='contentParent')
    content_status = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='contentStatus')
    content_type = sgqlc.types.Field(sgqlc.types.list_of(ContentTypeEnum), graphql_name='contentType')
    include_unapproved = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='includeUnapproved')
    karma = sgqlc.types.Field(Int, graphql_name='karma')
    order = sgqlc.types.Field(OrderEnum, graphql_name='order')
    orderby = sgqlc.types.Field(CommentsConnectionOrderbyEnum, graphql_name='orderby')
    parent = sgqlc.types.Field(Int, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    search = sgqlc.types.Field(String, graphql_name='search')
    status = sgqlc.types.Field(String, graphql_name='status')
    user_id = sgqlc.types.Field(ID, graphql_name='userId')


class UserToEventConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author', 'author_in', 'author_name', 'author_not_in', 'date_query', 'end_date_query', 'has_password', 'id', 'in_', 'mime_type', 'name', 'name_in', 'not_in', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'password', 'search', 'start_date_query', 'stati', 'status', 'tag', 'tag_id', 'tag_in', 'tag_not_in', 'tag_slug_and', 'tag_slug_in', 'title', 'venues_in', 'venues_not_in')
    author = sgqlc.types.Field(Int, graphql_name='author')
    author_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorIn')
    author_name = sgqlc.types.Field(String, graphql_name='authorName')
    author_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorNotIn')
    date_query = sgqlc.types.Field(DateQueryInput, graphql_name='dateQuery')
    end_date_query = sgqlc.types.Field(DateQueryInput, graphql_name='endDateQuery')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    id = sgqlc.types.Field(Int, graphql_name='id')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')
    mime_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='mimeType')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nameIn')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='notIn')
    orderby = sgqlc.types.Field(sgqlc.types.list_of(PostObjectsConnectionOrderbyInput), graphql_name='orderby')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    password = sgqlc.types.Field(String, graphql_name='password')
    search = sgqlc.types.Field(String, graphql_name='search')
    start_date_query = sgqlc.types.Field(DateQueryInput, graphql_name='startDateQuery')
    stati = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='stati')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    tag = sgqlc.types.Field(String, graphql_name='tag')
    tag_id = sgqlc.types.Field(String, graphql_name='tagId')
    tag_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='tagIn')
    tag_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='tagNotIn')
    tag_slug_and = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tagSlugAnd')
    tag_slug_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tagSlugIn')
    title = sgqlc.types.Field(String, graphql_name='title')
    venues_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='venuesIn')
    venues_not_in = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='venuesNotIn')


class UserToJobConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author', 'author_in', 'author_name', 'author_not_in', 'date_query', 'has_password', 'id', 'in_', 'mime_type', 'name', 'name_in', 'not_in', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'password', 'search', 'stati', 'status', 'title')
    author = sgqlc.types.Field(Int, graphql_name='author')
    author_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorIn')
    author_name = sgqlc.types.Field(String, graphql_name='authorName')
    author_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorNotIn')
    date_query = sgqlc.types.Field(DateQueryInput, graphql_name='dateQuery')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    id = sgqlc.types.Field(Int, graphql_name='id')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')
    mime_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='mimeType')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nameIn')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='notIn')
    orderby = sgqlc.types.Field(sgqlc.types.list_of(PostObjectsConnectionOrderbyInput), graphql_name='orderby')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    password = sgqlc.types.Field(String, graphql_name='password')
    search = sgqlc.types.Field(String, graphql_name='search')
    stati = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='stati')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class UserToMediaItemConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author', 'author_in', 'author_name', 'author_not_in', 'date_query', 'has_password', 'id', 'in_', 'mime_type', 'name', 'name_in', 'not_in', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'password', 'search', 'stati', 'status', 'title')
    author = sgqlc.types.Field(Int, graphql_name='author')
    author_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorIn')
    author_name = sgqlc.types.Field(String, graphql_name='authorName')
    author_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorNotIn')
    date_query = sgqlc.types.Field(DateQueryInput, graphql_name='dateQuery')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    id = sgqlc.types.Field(Int, graphql_name='id')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')
    mime_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='mimeType')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nameIn')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='notIn')
    orderby = sgqlc.types.Field(sgqlc.types.list_of(PostObjectsConnectionOrderbyInput), graphql_name='orderby')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    password = sgqlc.types.Field(String, graphql_name='password')
    search = sgqlc.types.Field(String, graphql_name='search')
    stati = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='stati')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class UserToOrganizerConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author', 'author_in', 'author_name', 'author_not_in', 'date_query', 'has_password', 'id', 'in_', 'mime_type', 'name', 'name_in', 'not_in', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'password', 'search', 'stati', 'status', 'title')
    author = sgqlc.types.Field(Int, graphql_name='author')
    author_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorIn')
    author_name = sgqlc.types.Field(String, graphql_name='authorName')
    author_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorNotIn')
    date_query = sgqlc.types.Field(DateQueryInput, graphql_name='dateQuery')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    id = sgqlc.types.Field(Int, graphql_name='id')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')
    mime_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='mimeType')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nameIn')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='notIn')
    orderby = sgqlc.types.Field(sgqlc.types.list_of(PostObjectsConnectionOrderbyInput), graphql_name='orderby')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    password = sgqlc.types.Field(String, graphql_name='password')
    search = sgqlc.types.Field(String, graphql_name='search')
    stati = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='stati')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class UserToPageConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author', 'author_in', 'author_name', 'author_not_in', 'date_query', 'has_password', 'id', 'in_', 'mime_type', 'name', 'name_in', 'not_in', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'password', 'search', 'stati', 'status', 'title')
    author = sgqlc.types.Field(Int, graphql_name='author')
    author_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorIn')
    author_name = sgqlc.types.Field(String, graphql_name='authorName')
    author_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorNotIn')
    date_query = sgqlc.types.Field(DateQueryInput, graphql_name='dateQuery')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    id = sgqlc.types.Field(Int, graphql_name='id')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')
    mime_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='mimeType')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nameIn')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='notIn')
    orderby = sgqlc.types.Field(sgqlc.types.list_of(PostObjectsConnectionOrderbyInput), graphql_name='orderby')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    password = sgqlc.types.Field(String, graphql_name='password')
    search = sgqlc.types.Field(String, graphql_name='search')
    stati = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='stati')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class UserToPartnerConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author', 'author_in', 'author_name', 'author_not_in', 'date_query', 'has_password', 'id', 'in_', 'mime_type', 'name', 'name_in', 'not_in', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'password', 'search', 'stati', 'status', 'title')
    author = sgqlc.types.Field(Int, graphql_name='author')
    author_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorIn')
    author_name = sgqlc.types.Field(String, graphql_name='authorName')
    author_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorNotIn')
    date_query = sgqlc.types.Field(DateQueryInput, graphql_name='dateQuery')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    id = sgqlc.types.Field(Int, graphql_name='id')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')
    mime_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='mimeType')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nameIn')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='notIn')
    orderby = sgqlc.types.Field(sgqlc.types.list_of(PostObjectsConnectionOrderbyInput), graphql_name='orderby')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    password = sgqlc.types.Field(String, graphql_name='password')
    search = sgqlc.types.Field(String, graphql_name='search')
    stati = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='stati')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class UserToPostConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author', 'author_in', 'author_name', 'author_not_in', 'category_id', 'category_in', 'category_name', 'category_not_in', 'date_query', 'has_password', 'id', 'in_', 'mime_type', 'name', 'name_in', 'not_in', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'password', 'search', 'stati', 'status', 'tag', 'tag_id', 'tag_in', 'tag_not_in', 'tag_slug_and', 'tag_slug_in', 'title')
    author = sgqlc.types.Field(Int, graphql_name='author')
    author_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorIn')
    author_name = sgqlc.types.Field(String, graphql_name='authorName')
    author_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorNotIn')
    category_id = sgqlc.types.Field(Int, graphql_name='categoryId')
    category_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='categoryIn')
    category_name = sgqlc.types.Field(String, graphql_name='categoryName')
    category_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='categoryNotIn')
    date_query = sgqlc.types.Field(DateQueryInput, graphql_name='dateQuery')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    id = sgqlc.types.Field(Int, graphql_name='id')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')
    mime_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='mimeType')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nameIn')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='notIn')
    orderby = sgqlc.types.Field(sgqlc.types.list_of(PostObjectsConnectionOrderbyInput), graphql_name='orderby')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    password = sgqlc.types.Field(String, graphql_name='password')
    search = sgqlc.types.Field(String, graphql_name='search')
    stati = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='stati')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    tag = sgqlc.types.Field(String, graphql_name='tag')
    tag_id = sgqlc.types.Field(String, graphql_name='tagId')
    tag_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='tagIn')
    tag_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='tagNotIn')
    tag_slug_and = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tagSlugAnd')
    tag_slug_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tagSlugIn')
    title = sgqlc.types.Field(String, graphql_name='title')


class UserToRevisionsConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('content_types', 'date_query', 'has_password', 'id', 'in_', 'mime_type', 'name', 'name_in', 'not_in', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'password', 'search', 'stati', 'status', 'title')
    content_types = sgqlc.types.Field(sgqlc.types.list_of(ContentTypeEnum), graphql_name='contentTypes')
    date_query = sgqlc.types.Field(DateQueryInput, graphql_name='dateQuery')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    id = sgqlc.types.Field(Int, graphql_name='id')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')
    mime_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='mimeType')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nameIn')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='notIn')
    orderby = sgqlc.types.Field(sgqlc.types.list_of(PostObjectsConnectionOrderbyInput), graphql_name='orderby')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    password = sgqlc.types.Field(String, graphql_name='password')
    search = sgqlc.types.Field(String, graphql_name='search')
    stati = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='stati')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class UserToVenueConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author', 'author_in', 'author_name', 'author_not_in', 'date_query', 'has_password', 'id', 'in_', 'mime_type', 'name', 'name_in', 'not_in', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'password', 'search', 'stati', 'status', 'title')
    author = sgqlc.types.Field(Int, graphql_name='author')
    author_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorIn')
    author_name = sgqlc.types.Field(String, graphql_name='authorName')
    author_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorNotIn')
    date_query = sgqlc.types.Field(DateQueryInput, graphql_name='dateQuery')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    id = sgqlc.types.Field(Int, graphql_name='id')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')
    mime_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='mimeType')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nameIn')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='notIn')
    orderby = sgqlc.types.Field(sgqlc.types.list_of(PostObjectsConnectionOrderbyInput), graphql_name='orderby')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    password = sgqlc.types.Field(String, graphql_name='password')
    search = sgqlc.types.Field(String, graphql_name='search')
    stati = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='stati')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')


class UsersConnectionOrderbyInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('field', 'order')
    field = sgqlc.types.Field(sgqlc.types.non_null(UsersConnectionOrderbyEnum), graphql_name='field')
    order = sgqlc.types.Field(OrderEnum, graphql_name='order')


class VenueToRevisionConnectionWhereArgs(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('author', 'author_in', 'author_name', 'author_not_in', 'date_query', 'has_password', 'id', 'in_', 'mime_type', 'name', 'name_in', 'not_in', 'orderby', 'parent', 'parent_in', 'parent_not_in', 'password', 'search', 'stati', 'status', 'title')
    author = sgqlc.types.Field(Int, graphql_name='author')
    author_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorIn')
    author_name = sgqlc.types.Field(String, graphql_name='authorName')
    author_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='authorNotIn')
    date_query = sgqlc.types.Field(DateQueryInput, graphql_name='dateQuery')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    id = sgqlc.types.Field(Int, graphql_name='id')
    in_ = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='in')
    mime_type = sgqlc.types.Field(MimeTypeEnum, graphql_name='mimeType')
    name = sgqlc.types.Field(String, graphql_name='name')
    name_in = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='nameIn')
    not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='notIn')
    orderby = sgqlc.types.Field(sgqlc.types.list_of(PostObjectsConnectionOrderbyInput), graphql_name='orderby')
    parent = sgqlc.types.Field(ID, graphql_name='parent')
    parent_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentIn')
    parent_not_in = sgqlc.types.Field(sgqlc.types.list_of(ID), graphql_name='parentNotIn')
    password = sgqlc.types.Field(String, graphql_name='password')
    search = sgqlc.types.Field(String, graphql_name='search')
    stati = sgqlc.types.Field(sgqlc.types.list_of(PostStatusEnum), graphql_name='stati')
    status = sgqlc.types.Field(PostStatusEnum, graphql_name='status')
    title = sgqlc.types.Field(String, graphql_name='title')



########################################################################
# Output Objects and Interfaces
########################################################################
class AcfFieldGroup(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ()


class AcfFieldGroupFields(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ()


class Connection(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Edge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Node'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')


class ContentTemplate(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('template_name',)
    template_name = sgqlc.types.Field(String, graphql_name='templateName')


class DatabaseIdentifier(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('database_id',)
    database_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='databaseId')


class Edge(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(String, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Node'), graphql_name='node')


class EnqueuedAsset(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('after', 'before', 'conditional', 'dependencies', 'handle', 'id', 'src', 'version')
    after = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='after')
    before = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='before')
    conditional = sgqlc.types.Field(String, graphql_name='conditional')
    dependencies = sgqlc.types.Field(sgqlc.types.list_of('EnqueuedAsset'), graphql_name='dependencies')
    handle = sgqlc.types.Field(String, graphql_name='handle')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    src = sgqlc.types.Field(String, graphql_name='src')
    version = sgqlc.types.Field(String, graphql_name='version')


class Node(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class PageInfo(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('end_cursor', 'has_next_page', 'has_previous_page', 'start_cursor')
    end_cursor = sgqlc.types.Field(String, graphql_name='endCursor')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')
    start_cursor = sgqlc.types.Field(String, graphql_name='startCursor')


class Previewable(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('is_preview', 'preview_revision_database_id', 'preview_revision_id')
    is_preview = sgqlc.types.Field(Boolean, graphql_name='isPreview')
    preview_revision_database_id = sgqlc.types.Field(Int, graphql_name='previewRevisionDatabaseId')
    preview_revision_id = sgqlc.types.Field(ID, graphql_name='previewRevisionId')


class WithAcfJobAcf(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('job_acf',)
    job_acf = sgqlc.types.Field('JobAcf', graphql_name='jobAcf')


class WithAcfPartnerAcf(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('partner_acf',)
    partner_acf = sgqlc.types.Field('PartnerAcf', graphql_name='partnerAcf')


class CategoryConnection(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CategoryConnectionEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Category'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('CategoryConnectionPageInfo'), graphql_name='pageInfo')


class CategoryConnectionEdge(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(String, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Category'), graphql_name='node')


class CategoryConnectionPageInfo(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('end_cursor', 'has_next_page', 'has_previous_page', 'start_cursor', 'total')
    end_cursor = sgqlc.types.Field(String, graphql_name='endCursor')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')
    start_cursor = sgqlc.types.Field(String, graphql_name='startCursor')
    total = sgqlc.types.Field(Int, graphql_name='total')


class CommentConnection(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CommentConnectionEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Comment'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('CommentConnectionPageInfo'), graphql_name='pageInfo')


class CommentConnectionEdge(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(String, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Comment'), graphql_name='node')


class CommentConnectionPageInfo(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('end_cursor', 'has_next_page', 'has_previous_page', 'start_cursor', 'total')
    end_cursor = sgqlc.types.Field(String, graphql_name='endCursor')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')
    start_cursor = sgqlc.types.Field(String, graphql_name='startCursor')
    total = sgqlc.types.Field(Int, graphql_name='total')


class Commenter(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('avatar', 'database_id', 'email', 'id', 'is_restricted', 'name', 'url')
    avatar = sgqlc.types.Field('Avatar', graphql_name='avatar')
    database_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='databaseId')
    email = sgqlc.types.Field(String, graphql_name='email')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_restricted = sgqlc.types.Field(Boolean, graphql_name='isRestricted')
    name = sgqlc.types.Field(String, graphql_name='name')
    url = sgqlc.types.Field(String, graphql_name='url')


class CommenterConnectionEdge(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(String, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(Commenter), graphql_name='node')


class ContentNode(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('content_type', 'content_type_name', 'database_id', 'date', 'date_gmt', 'desired_slug', 'editing_locked_by', 'enclosure', 'enqueued_scripts', 'enqueued_stylesheets', 'guid', 'id', 'is_comment', 'is_content_node', 'is_front_page', 'is_posts_page', 'is_preview', 'is_restricted', 'is_term_node', 'last_edited_by', 'link', 'modified', 'modified_gmt', 'preview_revision_database_id', 'preview_revision_id', 'slug', 'status', 'template', 'uri')
    content_type = sgqlc.types.Field('ContentNodeToContentTypeConnectionEdge', graphql_name='contentType')
    content_type_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='contentTypeName')
    database_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='databaseId')
    date = sgqlc.types.Field(String, graphql_name='date')
    date_gmt = sgqlc.types.Field(String, graphql_name='dateGmt')
    desired_slug = sgqlc.types.Field(String, graphql_name='desiredSlug')
    editing_locked_by = sgqlc.types.Field('ContentNodeToEditLockConnectionEdge', graphql_name='editingLockedBy')
    enclosure = sgqlc.types.Field(String, graphql_name='enclosure')
    enqueued_scripts = sgqlc.types.Field('ContentNodeToEnqueuedScriptConnection', graphql_name='enqueuedScripts', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    enqueued_stylesheets = sgqlc.types.Field('ContentNodeToEnqueuedStylesheetConnection', graphql_name='enqueuedStylesheets', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    guid = sgqlc.types.Field(String, graphql_name='guid')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_comment = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isComment')
    is_content_node = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isContentNode')
    is_front_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isFrontPage')
    is_posts_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPostsPage')
    is_preview = sgqlc.types.Field(Boolean, graphql_name='isPreview')
    is_restricted = sgqlc.types.Field(Boolean, graphql_name='isRestricted')
    is_term_node = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isTermNode')
    last_edited_by = sgqlc.types.Field('ContentNodeToEditLastConnectionEdge', graphql_name='lastEditedBy')
    link = sgqlc.types.Field(String, graphql_name='link')
    modified = sgqlc.types.Field(String, graphql_name='modified')
    modified_gmt = sgqlc.types.Field(String, graphql_name='modifiedGmt')
    preview_revision_database_id = sgqlc.types.Field(Int, graphql_name='previewRevisionDatabaseId')
    preview_revision_id = sgqlc.types.Field(ID, graphql_name='previewRevisionId')
    slug = sgqlc.types.Field(String, graphql_name='slug')
    status = sgqlc.types.Field(String, graphql_name='status')
    template = sgqlc.types.Field(ContentTemplate, graphql_name='template')
    uri = sgqlc.types.Field(String, graphql_name='uri')


class ContentNodeConnection(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ContentNodeConnectionEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ContentNode))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('ContentNodeConnectionPageInfo'), graphql_name='pageInfo')


class ContentNodeConnectionEdge(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(String, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(ContentNode), graphql_name='node')


class ContentNodeConnectionPageInfo(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('end_cursor', 'has_next_page', 'has_previous_page', 'start_cursor', 'total')
    end_cursor = sgqlc.types.Field(String, graphql_name='endCursor')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')
    start_cursor = sgqlc.types.Field(String, graphql_name='startCursor')
    total = sgqlc.types.Field(Int, graphql_name='total')


class ContentTypeConnection(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ContentTypeConnectionEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ContentType'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('ContentTypeConnectionPageInfo'), graphql_name='pageInfo')


class ContentTypeConnectionEdge(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(String, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('ContentType'), graphql_name='node')


class ContentTypeConnectionPageInfo(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('end_cursor', 'has_next_page', 'has_previous_page', 'start_cursor', 'total')
    end_cursor = sgqlc.types.Field(String, graphql_name='endCursor')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')
    start_cursor = sgqlc.types.Field(String, graphql_name='startCursor')
    total = sgqlc.types.Field(Int, graphql_name='total')


class ContractKindConnection(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ContractKindConnectionEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ContractKind'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('ContractKindConnectionPageInfo'), graphql_name='pageInfo')


class ContractKindConnectionEdge(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(String, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('ContractKind'), graphql_name='node')


class ContractKindConnectionPageInfo(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('end_cursor', 'has_next_page', 'has_previous_page', 'start_cursor', 'total')
    end_cursor = sgqlc.types.Field(String, graphql_name='endCursor')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')
    start_cursor = sgqlc.types.Field(String, graphql_name='startCursor')
    total = sgqlc.types.Field(Int, graphql_name='total')


class EnqueuedScriptConnection(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EnqueuedScriptConnectionEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EnqueuedScript'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('EnqueuedScriptConnectionPageInfo'), graphql_name='pageInfo')


class EnqueuedScriptConnectionEdge(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(String, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('EnqueuedScript'), graphql_name='node')


class EnqueuedScriptConnectionPageInfo(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('end_cursor', 'has_next_page', 'has_previous_page', 'start_cursor', 'total')
    end_cursor = sgqlc.types.Field(String, graphql_name='endCursor')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')
    start_cursor = sgqlc.types.Field(String, graphql_name='startCursor')
    total = sgqlc.types.Field(Int, graphql_name='total')


class EnqueuedStylesheetConnection(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EnqueuedStylesheetConnectionEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EnqueuedStylesheet'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('EnqueuedStylesheetConnectionPageInfo'), graphql_name='pageInfo')


class EnqueuedStylesheetConnectionEdge(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(String, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('EnqueuedStylesheet'), graphql_name='node')


class EnqueuedStylesheetConnectionPageInfo(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('end_cursor', 'has_next_page', 'has_previous_page', 'start_cursor', 'total')
    end_cursor = sgqlc.types.Field(String, graphql_name='endCursor')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')
    start_cursor = sgqlc.types.Field(String, graphql_name='startCursor')
    total = sgqlc.types.Field(Int, graphql_name='total')


class EventConnection(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EventConnectionEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Event'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('EventConnectionPageInfo'), graphql_name='pageInfo')


class EventConnectionEdge(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(String, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Event'), graphql_name='node')


class EventConnectionPageInfo(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('end_cursor', 'has_next_page', 'has_previous_page', 'start_cursor', 'total')
    end_cursor = sgqlc.types.Field(String, graphql_name='endCursor')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')
    start_cursor = sgqlc.types.Field(String, graphql_name='startCursor')
    total = sgqlc.types.Field(Int, graphql_name='total')


class EventsCategoryConnection(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EventsCategoryConnectionEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EventsCategory'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('EventsCategoryConnectionPageInfo'), graphql_name='pageInfo')


class EventsCategoryConnectionEdge(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(String, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('EventsCategory'), graphql_name='node')


class EventsCategoryConnectionPageInfo(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('end_cursor', 'has_next_page', 'has_previous_page', 'start_cursor', 'total')
    end_cursor = sgqlc.types.Field(String, graphql_name='endCursor')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')
    start_cursor = sgqlc.types.Field(String, graphql_name='startCursor')
    total = sgqlc.types.Field(Int, graphql_name='total')


class GraphqlDocumentConnection(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('GraphqlDocumentConnectionEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('GraphqlDocument'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('GraphqlDocumentConnectionPageInfo'), graphql_name='pageInfo')


class GraphqlDocumentConnectionEdge(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(String, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('GraphqlDocument'), graphql_name='node')


class GraphqlDocumentConnectionPageInfo(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('end_cursor', 'has_next_page', 'has_previous_page', 'start_cursor', 'total')
    end_cursor = sgqlc.types.Field(String, graphql_name='endCursor')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')
    start_cursor = sgqlc.types.Field(String, graphql_name='startCursor')
    total = sgqlc.types.Field(Int, graphql_name='total')


class GraphqlDocumentGroupConnection(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('GraphqlDocumentGroupConnectionEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('GraphqlDocumentGroup'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('GraphqlDocumentGroupConnectionPageInfo'), graphql_name='pageInfo')


class GraphqlDocumentGroupConnectionEdge(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(String, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('GraphqlDocumentGroup'), graphql_name='node')


class GraphqlDocumentGroupConnectionPageInfo(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('end_cursor', 'has_next_page', 'has_previous_page', 'start_cursor', 'total')
    end_cursor = sgqlc.types.Field(String, graphql_name='endCursor')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')
    start_cursor = sgqlc.types.Field(String, graphql_name='startCursor')
    total = sgqlc.types.Field(Int, graphql_name='total')


class HierarchicalNode(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('database_id', 'id', 'parent_database_id', 'parent_id')
    database_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='databaseId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    parent_database_id = sgqlc.types.Field(Int, graphql_name='parentDatabaseId')
    parent_id = sgqlc.types.Field(ID, graphql_name='parentId')


class HierarchicalContentNode(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('ancestors', 'children', 'content_type', 'content_type_name', 'database_id', 'date', 'date_gmt', 'desired_slug', 'editing_locked_by', 'enclosure', 'enqueued_scripts', 'enqueued_stylesheets', 'guid', 'id', 'is_comment', 'is_content_node', 'is_front_page', 'is_posts_page', 'is_preview', 'is_restricted', 'is_term_node', 'last_edited_by', 'link', 'modified', 'modified_gmt', 'parent', 'parent_database_id', 'parent_id', 'preview_revision_database_id', 'preview_revision_id', 'slug', 'status', 'template', 'uri')
    ancestors = sgqlc.types.Field('HierarchicalContentNodeToContentNodeAncestorsConnection', graphql_name='ancestors', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(HierarchicalContentNodeToContentNodeAncestorsConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    children = sgqlc.types.Field('HierarchicalContentNodeToContentNodeChildrenConnection', graphql_name='children', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(HierarchicalContentNodeToContentNodeChildrenConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    content_type = sgqlc.types.Field('ContentNodeToContentTypeConnectionEdge', graphql_name='contentType')
    content_type_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='contentTypeName')
    database_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='databaseId')
    date = sgqlc.types.Field(String, graphql_name='date')
    date_gmt = sgqlc.types.Field(String, graphql_name='dateGmt')
    desired_slug = sgqlc.types.Field(String, graphql_name='desiredSlug')
    editing_locked_by = sgqlc.types.Field('ContentNodeToEditLockConnectionEdge', graphql_name='editingLockedBy')
    enclosure = sgqlc.types.Field(String, graphql_name='enclosure')
    enqueued_scripts = sgqlc.types.Field('ContentNodeToEnqueuedScriptConnection', graphql_name='enqueuedScripts', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    enqueued_stylesheets = sgqlc.types.Field('ContentNodeToEnqueuedStylesheetConnection', graphql_name='enqueuedStylesheets', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    guid = sgqlc.types.Field(String, graphql_name='guid')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_comment = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isComment')
    is_content_node = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isContentNode')
    is_front_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isFrontPage')
    is_posts_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPostsPage')
    is_preview = sgqlc.types.Field(Boolean, graphql_name='isPreview')
    is_restricted = sgqlc.types.Field(Boolean, graphql_name='isRestricted')
    is_term_node = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isTermNode')
    last_edited_by = sgqlc.types.Field('ContentNodeToEditLastConnectionEdge', graphql_name='lastEditedBy')
    link = sgqlc.types.Field(String, graphql_name='link')
    modified = sgqlc.types.Field(String, graphql_name='modified')
    modified_gmt = sgqlc.types.Field(String, graphql_name='modifiedGmt')
    parent = sgqlc.types.Field('HierarchicalContentNodeToParentContentNodeConnectionEdge', graphql_name='parent')
    parent_database_id = sgqlc.types.Field(Int, graphql_name='parentDatabaseId')
    parent_id = sgqlc.types.Field(ID, graphql_name='parentId')
    preview_revision_database_id = sgqlc.types.Field(Int, graphql_name='previewRevisionDatabaseId')
    preview_revision_id = sgqlc.types.Field(ID, graphql_name='previewRevisionId')
    slug = sgqlc.types.Field(String, graphql_name='slug')
    status = sgqlc.types.Field(String, graphql_name='status')
    template = sgqlc.types.Field(ContentTemplate, graphql_name='template')
    uri = sgqlc.types.Field(String, graphql_name='uri')


class HierarchicalTermNode(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('count', 'database_id', 'description', 'enqueued_scripts', 'enqueued_stylesheets', 'id', 'is_comment', 'is_content_node', 'is_front_page', 'is_posts_page', 'is_restricted', 'is_term_node', 'link', 'name', 'parent_database_id', 'parent_id', 'slug', 'taxonomy_name', 'term_group_id', 'term_taxonomy_id', 'uri')
    count = sgqlc.types.Field(Int, graphql_name='count')
    database_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='databaseId')
    description = sgqlc.types.Field(String, graphql_name='description')
    enqueued_scripts = sgqlc.types.Field('TermNodeToEnqueuedScriptConnection', graphql_name='enqueuedScripts', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    enqueued_stylesheets = sgqlc.types.Field('TermNodeToEnqueuedStylesheetConnection', graphql_name='enqueuedStylesheets', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_comment = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isComment')
    is_content_node = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isContentNode')
    is_front_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isFrontPage')
    is_posts_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPostsPage')
    is_restricted = sgqlc.types.Field(Boolean, graphql_name='isRestricted')
    is_term_node = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isTermNode')
    link = sgqlc.types.Field(String, graphql_name='link')
    name = sgqlc.types.Field(String, graphql_name='name')
    parent_database_id = sgqlc.types.Field(Int, graphql_name='parentDatabaseId')
    parent_id = sgqlc.types.Field(ID, graphql_name='parentId')
    slug = sgqlc.types.Field(String, graphql_name='slug')
    taxonomy_name = sgqlc.types.Field(String, graphql_name='taxonomyName')
    term_group_id = sgqlc.types.Field(Int, graphql_name='termGroupId')
    term_taxonomy_id = sgqlc.types.Field(Int, graphql_name='termTaxonomyId')
    uri = sgqlc.types.Field(String, graphql_name='uri')


class JobAcf_Fields(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('apply_link', 'compagny_logo', 'compagny_name', 'description', 'job_contact_email', 'job_title', 'job_type_of_contract', 'job_type_of_post', 'localization', 'post_sheet', 'presence')
    apply_link = sgqlc.types.Field(String, graphql_name='applyLink')
    compagny_logo = sgqlc.types.Field('AcfMediaItemConnectionEdge', graphql_name='compagnyLogo')
    compagny_name = sgqlc.types.Field(String, graphql_name='compagnyName')
    description = sgqlc.types.Field(String, graphql_name='description')
    job_contact_email = sgqlc.types.Field(String, graphql_name='jobContactEmail')
    job_title = sgqlc.types.Field(String, graphql_name='jobTitle')
    job_type_of_contract = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='jobTypeOfContract')
    job_type_of_post = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='jobTypeOfPost')
    localization = sgqlc.types.Field(String, graphql_name='localization')
    post_sheet = sgqlc.types.Field('AcfMediaItemConnectionEdge', graphql_name='postSheet')
    presence = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='presence')


class JobConnection(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('JobConnectionEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Job'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('JobConnectionPageInfo'), graphql_name='pageInfo')


class JobConnectionEdge(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(String, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Job'), graphql_name='node')


class JobConnectionPageInfo(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('end_cursor', 'has_next_page', 'has_previous_page', 'start_cursor', 'total')
    end_cursor = sgqlc.types.Field(String, graphql_name='endCursor')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')
    start_cursor = sgqlc.types.Field(String, graphql_name='startCursor')
    total = sgqlc.types.Field(Int, graphql_name='total')


class JobmodeConnection(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('JobmodeConnectionEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Jobmode'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('JobmodeConnectionPageInfo'), graphql_name='pageInfo')


class JobmodeConnectionEdge(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(String, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Jobmode'), graphql_name='node')


class JobmodeConnectionPageInfo(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('end_cursor', 'has_next_page', 'has_previous_page', 'start_cursor', 'total')
    end_cursor = sgqlc.types.Field(String, graphql_name='endCursor')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')
    start_cursor = sgqlc.types.Field(String, graphql_name='startCursor')
    total = sgqlc.types.Field(Int, graphql_name='total')


class MediaItemConnection(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('MediaItemConnectionEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('MediaItem'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('MediaItemConnectionPageInfo'), graphql_name='pageInfo')


class MediaItemConnectionEdge(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(String, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('MediaItem'), graphql_name='node')


class MediaItemConnectionPageInfo(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('end_cursor', 'has_next_page', 'has_previous_page', 'start_cursor', 'total')
    end_cursor = sgqlc.types.Field(String, graphql_name='endCursor')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')
    start_cursor = sgqlc.types.Field(String, graphql_name='startCursor')
    total = sgqlc.types.Field(Int, graphql_name='total')


class MenuConnection(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('MenuConnectionEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Menu'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('MenuConnectionPageInfo'), graphql_name='pageInfo')


class MenuConnectionEdge(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(String, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Menu'), graphql_name='node')


class MenuConnectionPageInfo(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('end_cursor', 'has_next_page', 'has_previous_page', 'start_cursor', 'total')
    end_cursor = sgqlc.types.Field(String, graphql_name='endCursor')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')
    start_cursor = sgqlc.types.Field(String, graphql_name='startCursor')
    total = sgqlc.types.Field(Int, graphql_name='total')


class MenuItemConnection(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('MenuItemConnectionEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('MenuItem'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('MenuItemConnectionPageInfo'), graphql_name='pageInfo')


class MenuItemConnectionEdge(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(String, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('MenuItem'), graphql_name='node')


class MenuItemConnectionPageInfo(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('end_cursor', 'has_next_page', 'has_previous_page', 'start_cursor', 'total')
    end_cursor = sgqlc.types.Field(String, graphql_name='endCursor')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')
    start_cursor = sgqlc.types.Field(String, graphql_name='startCursor')
    total = sgqlc.types.Field(Int, graphql_name='total')


class MenuItemLinkable(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('database_id', 'id', 'is_comment', 'is_content_node', 'is_front_page', 'is_posts_page', 'is_term_node', 'uri')
    database_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='databaseId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_comment = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isComment')
    is_content_node = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isContentNode')
    is_front_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isFrontPage')
    is_posts_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPostsPage')
    is_term_node = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isTermNode')
    uri = sgqlc.types.Field(String, graphql_name='uri')


class MenuItemLinkableConnectionEdge(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(String, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(MenuItemLinkable), graphql_name='node')


class NodeWithAuthor(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('author', 'author_database_id', 'author_id', 'id')
    author = sgqlc.types.Field('NodeWithAuthorToUserConnectionEdge', graphql_name='author')
    author_database_id = sgqlc.types.Field(Int, graphql_name='authorDatabaseId')
    author_id = sgqlc.types.Field(ID, graphql_name='authorId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class NodeWithComments(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('comment_count', 'comment_status', 'id')
    comment_count = sgqlc.types.Field(Int, graphql_name='commentCount')
    comment_status = sgqlc.types.Field(String, graphql_name='commentStatus')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class NodeWithContentEditor(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('content', 'id')
    content = sgqlc.types.Field(String, graphql_name='content', args=sgqlc.types.ArgDict((
        ('format', sgqlc.types.Arg(PostObjectFieldFormatEnum, graphql_name='format', default=None)),
))
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class NodeWithExcerpt(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('excerpt', 'id')
    excerpt = sgqlc.types.Field(String, graphql_name='excerpt', args=sgqlc.types.ArgDict((
        ('format', sgqlc.types.Arg(PostObjectFieldFormatEnum, graphql_name='format', default=None)),
))
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class NodeWithFeaturedImage(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('featured_image', 'featured_image_database_id', 'featured_image_id', 'id')
    featured_image = sgqlc.types.Field('NodeWithFeaturedImageToMediaItemConnectionEdge', graphql_name='featuredImage')
    featured_image_database_id = sgqlc.types.Field(Int, graphql_name='featuredImageDatabaseId')
    featured_image_id = sgqlc.types.Field(ID, graphql_name='featuredImageId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class NodeWithPageAttributes(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('id', 'menu_order')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    menu_order = sgqlc.types.Field(Int, graphql_name='menuOrder')


class NodeWithRevisions(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('id', 'is_revision', 'revision_of')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_revision = sgqlc.types.Field(Boolean, graphql_name='isRevision')
    revision_of = sgqlc.types.Field('NodeWithRevisionsToContentNodeConnectionEdge', graphql_name='revisionOf')


class NodeWithTemplate(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('id', 'template')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    template = sgqlc.types.Field(ContentTemplate, graphql_name='template')


class NodeWithTitle(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('id', 'title')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    title = sgqlc.types.Field(String, graphql_name='title', args=sgqlc.types.ArgDict((
        ('format', sgqlc.types.Arg(PostObjectFieldFormatEnum, graphql_name='format', default=None)),
))
    )


class NodeWithTrackbacks(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('id', 'ping_status', 'pinged', 'to_ping')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    ping_status = sgqlc.types.Field(String, graphql_name='pingStatus')
    pinged = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='pinged')
    to_ping = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='toPing')


class OccupationkindConnection(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('OccupationkindConnectionEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Occupationkind'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('OccupationkindConnectionPageInfo'), graphql_name='pageInfo')


class OccupationkindConnectionEdge(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(String, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Occupationkind'), graphql_name='node')


class OccupationkindConnectionPageInfo(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('end_cursor', 'has_next_page', 'has_previous_page', 'start_cursor', 'total')
    end_cursor = sgqlc.types.Field(String, graphql_name='endCursor')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')
    start_cursor = sgqlc.types.Field(String, graphql_name='startCursor')
    total = sgqlc.types.Field(Int, graphql_name='total')


class OneToOneConnection(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(String, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(Node), graphql_name='node')


class OrganizerConnection(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('OrganizerConnectionEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Organizer'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('OrganizerConnectionPageInfo'), graphql_name='pageInfo')


class OrganizerConnectionEdge(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(String, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Organizer'), graphql_name='node')


class OrganizerConnectionPageInfo(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('end_cursor', 'has_next_page', 'has_previous_page', 'start_cursor', 'total')
    end_cursor = sgqlc.types.Field(String, graphql_name='endCursor')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')
    start_cursor = sgqlc.types.Field(String, graphql_name='startCursor')
    total = sgqlc.types.Field(Int, graphql_name='total')


class PageConnection(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PageConnectionEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Page'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageConnectionPageInfo'), graphql_name='pageInfo')


class PageConnectionEdge(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(String, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Page'), graphql_name='node')


class PageConnectionPageInfo(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('end_cursor', 'has_next_page', 'has_previous_page', 'start_cursor', 'total')
    end_cursor = sgqlc.types.Field(String, graphql_name='endCursor')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')
    start_cursor = sgqlc.types.Field(String, graphql_name='startCursor')
    total = sgqlc.types.Field(Int, graphql_name='total')


class PartnerAcf_Fields(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('partner_description', 'partner_logo', 'partner_name', 'partner_website_link', 'technologie', 'type_of_company')
    partner_description = sgqlc.types.Field(String, graphql_name='partnerDescription')
    partner_logo = sgqlc.types.Field('AcfMediaItemConnectionEdge', graphql_name='partnerLogo')
    partner_name = sgqlc.types.Field(String, graphql_name='partnerName')
    partner_website_link = sgqlc.types.Field(String, graphql_name='partnerWebsiteLink')
    technologie = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='technologie')
    type_of_company = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='typeOfCompany')


class PartnerConnection(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PartnerConnectionEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Partner'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PartnerConnectionPageInfo'), graphql_name='pageInfo')


class PartnerConnectionEdge(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(String, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Partner'), graphql_name='node')


class PartnerConnectionPageInfo(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('end_cursor', 'has_next_page', 'has_previous_page', 'start_cursor', 'total')
    end_cursor = sgqlc.types.Field(String, graphql_name='endCursor')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')
    start_cursor = sgqlc.types.Field(String, graphql_name='startCursor')
    total = sgqlc.types.Field(Int, graphql_name='total')


class PluginConnection(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PluginConnectionEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Plugin'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PluginConnectionPageInfo'), graphql_name='pageInfo')


class PluginConnectionEdge(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(String, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Plugin'), graphql_name='node')


class PluginConnectionPageInfo(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('end_cursor', 'has_next_page', 'has_previous_page', 'start_cursor', 'total')
    end_cursor = sgqlc.types.Field(String, graphql_name='endCursor')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')
    start_cursor = sgqlc.types.Field(String, graphql_name='startCursor')
    total = sgqlc.types.Field(Int, graphql_name='total')


class PostConnection(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PostConnectionEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Post'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PostConnectionPageInfo'), graphql_name='pageInfo')


class PostConnectionEdge(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(String, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Post'), graphql_name='node')


class PostConnectionPageInfo(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('end_cursor', 'has_next_page', 'has_previous_page', 'start_cursor', 'total')
    end_cursor = sgqlc.types.Field(String, graphql_name='endCursor')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')
    start_cursor = sgqlc.types.Field(String, graphql_name='startCursor')
    total = sgqlc.types.Field(Int, graphql_name='total')


class PostFormatConnection(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PostFormatConnectionEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PostFormat'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PostFormatConnectionPageInfo'), graphql_name='pageInfo')


class PostFormatConnectionEdge(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(String, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('PostFormat'), graphql_name='node')


class TagConnection(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TagConnectionEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Tag'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('TagConnectionPageInfo'), graphql_name='pageInfo')


class TagConnectionEdge(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(String, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Tag'), graphql_name='node')


class TagConnectionPageInfo(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('end_cursor', 'has_next_page', 'has_previous_page', 'start_cursor', 'total')
    end_cursor = sgqlc.types.Field(String, graphql_name='endCursor')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')
    start_cursor = sgqlc.types.Field(String, graphql_name='startCursor')
    total = sgqlc.types.Field(Int, graphql_name='total')


class TaxonomyConnection(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TaxonomyConnectionEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Taxonomy'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('TaxonomyConnectionPageInfo'), graphql_name='pageInfo')


class TaxonomyConnectionEdge(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(String, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Taxonomy'), graphql_name='node')


class TaxonomyConnectionPageInfo(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('end_cursor', 'has_next_page', 'has_previous_page', 'start_cursor', 'total')
    end_cursor = sgqlc.types.Field(String, graphql_name='endCursor')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')
    start_cursor = sgqlc.types.Field(String, graphql_name='startCursor')
    total = sgqlc.types.Field(Int, graphql_name='total')


class TermNode(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('count', 'database_id', 'description', 'enqueued_scripts', 'enqueued_stylesheets', 'id', 'is_comment', 'is_content_node', 'is_front_page', 'is_posts_page', 'is_restricted', 'is_term_node', 'link', 'name', 'slug', 'taxonomy_name', 'term_group_id', 'term_taxonomy_id', 'uri')
    count = sgqlc.types.Field(Int, graphql_name='count')
    database_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='databaseId')
    description = sgqlc.types.Field(String, graphql_name='description')
    enqueued_scripts = sgqlc.types.Field('TermNodeToEnqueuedScriptConnection', graphql_name='enqueuedScripts', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    enqueued_stylesheets = sgqlc.types.Field('TermNodeToEnqueuedStylesheetConnection', graphql_name='enqueuedStylesheets', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_comment = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isComment')
    is_content_node = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isContentNode')
    is_front_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isFrontPage')
    is_posts_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPostsPage')
    is_restricted = sgqlc.types.Field(Boolean, graphql_name='isRestricted')
    is_term_node = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isTermNode')
    link = sgqlc.types.Field(String, graphql_name='link')
    name = sgqlc.types.Field(String, graphql_name='name')
    slug = sgqlc.types.Field(String, graphql_name='slug')
    taxonomy_name = sgqlc.types.Field(String, graphql_name='taxonomyName')
    term_group_id = sgqlc.types.Field(Int, graphql_name='termGroupId')
    term_taxonomy_id = sgqlc.types.Field(Int, graphql_name='termTaxonomyId')
    uri = sgqlc.types.Field(String, graphql_name='uri')


class TermNodeConnection(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TermNodeConnectionEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TermNode))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('TermNodeConnectionPageInfo'), graphql_name='pageInfo')


class TermNodeConnectionEdge(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(String, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(TermNode), graphql_name='node')


class TermNodeConnectionPageInfo(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('end_cursor', 'has_next_page', 'has_previous_page', 'start_cursor', 'total')
    end_cursor = sgqlc.types.Field(String, graphql_name='endCursor')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')
    start_cursor = sgqlc.types.Field(String, graphql_name='startCursor')
    total = sgqlc.types.Field(Int, graphql_name='total')


class ThemeConnection(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ThemeConnectionEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Theme'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('ThemeConnectionPageInfo'), graphql_name='pageInfo')


class ThemeConnectionEdge(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(String, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Theme'), graphql_name='node')


class ThemeConnectionPageInfo(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('end_cursor', 'has_next_page', 'has_previous_page', 'start_cursor', 'total')
    end_cursor = sgqlc.types.Field(String, graphql_name='endCursor')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')
    start_cursor = sgqlc.types.Field(String, graphql_name='startCursor')
    total = sgqlc.types.Field(Int, graphql_name='total')


class UniformResourceIdentifiable(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('id', 'is_comment', 'is_content_node', 'is_front_page', 'is_posts_page', 'is_term_node', 'uri')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_comment = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isComment')
    is_content_node = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isContentNode')
    is_front_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isFrontPage')
    is_posts_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPostsPage')
    is_term_node = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isTermNode')
    uri = sgqlc.types.Field(String, graphql_name='uri')


class UserConnection(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserConnectionEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('User'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('UserConnectionPageInfo'), graphql_name='pageInfo')


class UserConnectionEdge(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(String, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='node')


class UserConnectionPageInfo(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('end_cursor', 'has_next_page', 'has_previous_page', 'start_cursor', 'total')
    end_cursor = sgqlc.types.Field(String, graphql_name='endCursor')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')
    start_cursor = sgqlc.types.Field(String, graphql_name='startCursor')
    total = sgqlc.types.Field(Int, graphql_name='total')


class UserRoleConnection(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserRoleConnectionEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserRole'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('UserRoleConnectionPageInfo'), graphql_name='pageInfo')


class UserRoleConnectionEdge(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(String, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('UserRole'), graphql_name='node')


class VenueConnection(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('VenueConnectionEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Venue'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('VenueConnectionPageInfo'), graphql_name='pageInfo')


class VenueConnectionEdge(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(String, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Venue'), graphql_name='node')


class WPPageInfo(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('end_cursor', 'has_next_page', 'has_previous_page', 'start_cursor', 'total')
    end_cursor = sgqlc.types.Field(String, graphql_name='endCursor')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')
    start_cursor = sgqlc.types.Field(String, graphql_name='startCursor')
    total = sgqlc.types.Field(Int, graphql_name='total')


class PostFormatConnectionPageInfo(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('end_cursor', 'has_next_page', 'has_previous_page', 'start_cursor', 'total')
    end_cursor = sgqlc.types.Field(String, graphql_name='endCursor')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')
    start_cursor = sgqlc.types.Field(String, graphql_name='startCursor')
    total = sgqlc.types.Field(Int, graphql_name='total')


class UserRoleConnectionPageInfo(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('end_cursor', 'has_next_page', 'has_previous_page', 'start_cursor', 'total')
    end_cursor = sgqlc.types.Field(String, graphql_name='endCursor')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')
    start_cursor = sgqlc.types.Field(String, graphql_name='startCursor')
    total = sgqlc.types.Field(Int, graphql_name='total')


class VenueConnectionPageInfo(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('end_cursor', 'has_next_page', 'has_previous_page', 'start_cursor', 'total')
    end_cursor = sgqlc.types.Field(String, graphql_name='endCursor')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')
    start_cursor = sgqlc.types.Field(String, graphql_name='startCursor')
    total = sgqlc.types.Field(Int, graphql_name='total')


class AddressLinkedData(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('address_country', 'address_locality', 'address_region', 'postal_code', 'street_address', 'type')
    address_country = sgqlc.types.Field(String, graphql_name='addressCountry')
    address_locality = sgqlc.types.Field(String, graphql_name='addressLocality')
    address_region = sgqlc.types.Field(String, graphql_name='addressRegion')
    postal_code = sgqlc.types.Field(String, graphql_name='postalCode')
    street_address = sgqlc.types.Field(String, graphql_name='streetAddress')
    type = sgqlc.types.Field(String, graphql_name='type')


class Avatar(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('default', 'extra_attr', 'force_default', 'found_avatar', 'height', 'is_restricted', 'rating', 'scheme', 'size', 'url', 'width')
    default = sgqlc.types.Field(String, graphql_name='default')
    extra_attr = sgqlc.types.Field(String, graphql_name='extraAttr')
    force_default = sgqlc.types.Field(Boolean, graphql_name='forceDefault')
    found_avatar = sgqlc.types.Field(Boolean, graphql_name='foundAvatar')
    height = sgqlc.types.Field(Int, graphql_name='height')
    is_restricted = sgqlc.types.Field(Boolean, graphql_name='isRestricted')
    rating = sgqlc.types.Field(String, graphql_name='rating')
    scheme = sgqlc.types.Field(String, graphql_name='scheme')
    size = sgqlc.types.Field(Int, graphql_name='size')
    url = sgqlc.types.Field(String, graphql_name='url')
    width = sgqlc.types.Field(Int, graphql_name='width')


class CreateCategoryPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('category', 'client_mutation_id')
    category = sgqlc.types.Field('Category', graphql_name='category')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class CreateCommentPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'comment', 'success')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    comment = sgqlc.types.Field('Comment', graphql_name='comment')
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class CreateContractKindPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'contract_kind')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    contract_kind = sgqlc.types.Field('ContractKind', graphql_name='contractKind')


class CreateEventPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('event', 'client_mutation_id')
    event = sgqlc.types.Field('Event', graphql_name='event')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class CreateEventsCategoryPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('events_category', 'client_mutation_id')
    events_category = sgqlc.types.Field('EventsCategory', graphql_name='eventsCategory')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class CreateGraphqlDocumentGroupPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'graphql_document_group')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    graphql_document_group = sgqlc.types.Field('GraphqlDocumentGroup', graphql_name='graphqlDocumentGroup')


class CreateGraphqlDocumentPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'graphql_document')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    graphql_document = sgqlc.types.Field('GraphqlDocument', graphql_name='graphqlDocument')


class CreateJobPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'job')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    job = sgqlc.types.Field('Job', graphql_name='job')


class CreateJobmodePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'jobmode')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    jobmode = sgqlc.types.Field('Jobmode', graphql_name='jobmode')


class CreateMediaItemPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'media_item')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    media_item = sgqlc.types.Field('MediaItem', graphql_name='mediaItem')


class CreateOccupationkindPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'occupationkind')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    occupationkind = sgqlc.types.Field('Occupationkind', graphql_name='occupationkind')


class CreateOrganizerPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('organizer', 'client_mutation_id')
    organizer = sgqlc.types.Field('Organizer', graphql_name='organizer')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class CreatePagePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'page')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    page = sgqlc.types.Field('Page', graphql_name='page')


class CreatePartnerPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'partner')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    partner = sgqlc.types.Field('Partner', graphql_name='partner')


class CreatePostFormatPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'post_format')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    post_format = sgqlc.types.Field('PostFormat', graphql_name='postFormat')


class CreatePostPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'post')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    post = sgqlc.types.Field('Post', graphql_name='post')


class CreateTagPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'tag')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    tag = sgqlc.types.Field('Tag', graphql_name='tag')


class CreateUserPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'user')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    user = sgqlc.types.Field('User', graphql_name='user')


class CreateVenuePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('venue', 'client_mutation_id')
    venue = sgqlc.types.Field('Venue', graphql_name='venue')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class DeleteCategoryPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('category', 'client_mutation_id', 'deleted_id')
    category = sgqlc.types.Field('Category', graphql_name='category')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    deleted_id = sgqlc.types.Field(ID, graphql_name='deletedId')


class DeleteCommentPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'comment', 'deleted_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    comment = sgqlc.types.Field('Comment', graphql_name='comment')
    deleted_id = sgqlc.types.Field(ID, graphql_name='deletedId')


class DeleteContractKindPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'contract_kind', 'deleted_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    contract_kind = sgqlc.types.Field('ContractKind', graphql_name='contractKind')
    deleted_id = sgqlc.types.Field(ID, graphql_name='deletedId')


class DeleteEventPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('event', 'client_mutation_id', 'deleted_id')
    event = sgqlc.types.Field('Event', graphql_name='event')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    deleted_id = sgqlc.types.Field(ID, graphql_name='deletedId')


class DeleteEventsCategoryPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('events_category', 'client_mutation_id', 'deleted_id')
    events_category = sgqlc.types.Field('EventsCategory', graphql_name='eventsCategory')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    deleted_id = sgqlc.types.Field(ID, graphql_name='deletedId')


class DeleteGraphqlDocumentGroupPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'deleted_id', 'graphql_document_group')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    deleted_id = sgqlc.types.Field(ID, graphql_name='deletedId')
    graphql_document_group = sgqlc.types.Field('GraphqlDocumentGroup', graphql_name='graphqlDocumentGroup')


class DeleteGraphqlDocumentPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'deleted_id', 'graphql_document')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    deleted_id = sgqlc.types.Field(ID, graphql_name='deletedId')
    graphql_document = sgqlc.types.Field('GraphqlDocument', graphql_name='graphqlDocument')


class DeleteJobPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'deleted_id', 'job')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    deleted_id = sgqlc.types.Field(ID, graphql_name='deletedId')
    job = sgqlc.types.Field('Job', graphql_name='job')


class DeleteJobmodePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'deleted_id', 'jobmode')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    deleted_id = sgqlc.types.Field(ID, graphql_name='deletedId')
    jobmode = sgqlc.types.Field('Jobmode', graphql_name='jobmode')


class DeleteMediaItemPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'deleted_id', 'media_item')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    deleted_id = sgqlc.types.Field(ID, graphql_name='deletedId')
    media_item = sgqlc.types.Field('MediaItem', graphql_name='mediaItem')


class DeleteOccupationkindPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'deleted_id', 'occupationkind')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    deleted_id = sgqlc.types.Field(ID, graphql_name='deletedId')
    occupationkind = sgqlc.types.Field('Occupationkind', graphql_name='occupationkind')


class DeleteOrganizerPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('organizer', 'client_mutation_id', 'deleted_id')
    organizer = sgqlc.types.Field('Organizer', graphql_name='organizer')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    deleted_id = sgqlc.types.Field(ID, graphql_name='deletedId')


class DeletePagePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'deleted_id', 'page')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    deleted_id = sgqlc.types.Field(ID, graphql_name='deletedId')
    page = sgqlc.types.Field('Page', graphql_name='page')


class DeletePartnerPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'deleted_id', 'partner')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    deleted_id = sgqlc.types.Field(ID, graphql_name='deletedId')
    partner = sgqlc.types.Field('Partner', graphql_name='partner')


class DeletePostFormatPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'deleted_id', 'post_format')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    deleted_id = sgqlc.types.Field(ID, graphql_name='deletedId')
    post_format = sgqlc.types.Field('PostFormat', graphql_name='postFormat')


class DeletePostPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'deleted_id', 'post')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    deleted_id = sgqlc.types.Field(ID, graphql_name='deletedId')
    post = sgqlc.types.Field('Post', graphql_name='post')


class DeleteTagPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'deleted_id', 'tag')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    deleted_id = sgqlc.types.Field(ID, graphql_name='deletedId')
    tag = sgqlc.types.Field('Tag', graphql_name='tag')


class DeleteUserPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'deleted_id', 'user')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    deleted_id = sgqlc.types.Field(ID, graphql_name='deletedId')
    user = sgqlc.types.Field('User', graphql_name='user')


class DeleteVenuePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('venue', 'client_mutation_id', 'deleted_id')
    venue = sgqlc.types.Field('Venue', graphql_name='venue')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    deleted_id = sgqlc.types.Field(ID, graphql_name='deletedId')


class DiscussionSettings(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('default_comment_status', 'default_ping_status')
    default_comment_status = sgqlc.types.Field(String, graphql_name='defaultCommentStatus')
    default_ping_status = sgqlc.types.Field(String, graphql_name='defaultPingStatus')


class EventLinkedData(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('context', 'description', 'end_date', 'location', 'name', 'organizer', 'performer', 'start_date', 'type', 'url')
    context = sgqlc.types.Field(String, graphql_name='context')
    description = sgqlc.types.Field(String, graphql_name='description')
    end_date = sgqlc.types.Field(String, graphql_name='endDate')
    location = sgqlc.types.Field('VenueLinkedData', graphql_name='location')
    name = sgqlc.types.Field(String, graphql_name='name')
    organizer = sgqlc.types.Field('OrganizerLinkedData', graphql_name='organizer')
    performer = sgqlc.types.Field(String, graphql_name='performer')
    start_date = sgqlc.types.Field(String, graphql_name='startDate')
    type = sgqlc.types.Field(String, graphql_name='type')
    url = sgqlc.types.Field(String, graphql_name='url')


class GeneralSettings(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('date_format', 'description', 'email', 'language', 'start_of_week', 'time_format', 'timezone', 'title', 'url')
    date_format = sgqlc.types.Field(String, graphql_name='dateFormat')
    description = sgqlc.types.Field(String, graphql_name='description')
    email = sgqlc.types.Field(String, graphql_name='email')
    language = sgqlc.types.Field(String, graphql_name='language')
    start_of_week = sgqlc.types.Field(Int, graphql_name='startOfWeek')
    time_format = sgqlc.types.Field(String, graphql_name='timeFormat')
    timezone = sgqlc.types.Field(String, graphql_name='timezone')
    title = sgqlc.types.Field(String, graphql_name='title')
    url = sgqlc.types.Field(String, graphql_name='url')


class LoginPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('auth_token', 'client_mutation_id', 'refresh_token', 'user')
    auth_token = sgqlc.types.Field(String, graphql_name='authToken')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    refresh_token = sgqlc.types.Field(String, graphql_name='refreshToken')
    user = sgqlc.types.Field('User', graphql_name='user')


class MediaDetails(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('file', 'height', 'meta', 'sizes', 'width')
    file = sgqlc.types.Field(String, graphql_name='file')
    height = sgqlc.types.Field(Int, graphql_name='height')
    meta = sgqlc.types.Field('MediaItemMeta', graphql_name='meta')
    sizes = sgqlc.types.Field(sgqlc.types.list_of('MediaSize'), graphql_name='sizes', args=sgqlc.types.ArgDict((
        ('exclude', sgqlc.types.Arg(sgqlc.types.list_of(MediaItemSizeEnum), graphql_name='exclude', default=None)),
        ('include', sgqlc.types.Arg(sgqlc.types.list_of(MediaItemSizeEnum), graphql_name='include', default=None)),
))
    )
    width = sgqlc.types.Field(Int, graphql_name='width')


class MediaItemMeta(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('aperture', 'camera', 'caption', 'copyright', 'created_timestamp', 'credit', 'focal_length', 'iso', 'keywords', 'orientation', 'shutter_speed', 'title')
    aperture = sgqlc.types.Field(Float, graphql_name='aperture')
    camera = sgqlc.types.Field(String, graphql_name='camera')
    caption = sgqlc.types.Field(String, graphql_name='caption')
    copyright = sgqlc.types.Field(String, graphql_name='copyright')
    created_timestamp = sgqlc.types.Field(Int, graphql_name='createdTimestamp')
    credit = sgqlc.types.Field(String, graphql_name='credit')
    focal_length = sgqlc.types.Field(Float, graphql_name='focalLength')
    iso = sgqlc.types.Field(Int, graphql_name='iso')
    keywords = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='keywords')
    orientation = sgqlc.types.Field(String, graphql_name='orientation')
    shutter_speed = sgqlc.types.Field(Float, graphql_name='shutterSpeed')
    title = sgqlc.types.Field(String, graphql_name='title')


class MediaSize(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('file', 'file_size', 'height', 'mime_type', 'name', 'source_url', 'width')
    file = sgqlc.types.Field(String, graphql_name='file')
    file_size = sgqlc.types.Field(Int, graphql_name='fileSize')
    height = sgqlc.types.Field(String, graphql_name='height')
    mime_type = sgqlc.types.Field(String, graphql_name='mimeType')
    name = sgqlc.types.Field(String, graphql_name='name')
    source_url = sgqlc.types.Field(String, graphql_name='sourceUrl')
    width = sgqlc.types.Field(String, graphql_name='width')


class OrganizerLinkedData(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('description', 'email', 'name', 'same_as', 'telephone', 'type', 'url')
    description = sgqlc.types.Field(String, graphql_name='description')
    email = sgqlc.types.Field(String, graphql_name='email')
    name = sgqlc.types.Field(String, graphql_name='name')
    same_as = sgqlc.types.Field(String, graphql_name='sameAs')
    telephone = sgqlc.types.Field(String, graphql_name='telephone')
    type = sgqlc.types.Field(String, graphql_name='type')
    url = sgqlc.types.Field(String, graphql_name='url')


class PostTypeLabelDetails(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('add_new', 'add_new_item', 'all_items', 'archives', 'attributes', 'edit_item', 'featured_image', 'filter_items_list', 'insert_into_item', 'items_list', 'items_list_navigation', 'menu_name', 'name', 'new_item', 'not_found', 'not_found_in_trash', 'parent_item_colon', 'remove_featured_image', 'search_items', 'set_featured_image', 'singular_name', 'uploaded_to_this_item', 'use_featured_image', 'view_item', 'view_items')
    add_new = sgqlc.types.Field(String, graphql_name='addNew')
    add_new_item = sgqlc.types.Field(String, graphql_name='addNewItem')
    all_items = sgqlc.types.Field(String, graphql_name='allItems')
    archives = sgqlc.types.Field(String, graphql_name='archives')
    attributes = sgqlc.types.Field(String, graphql_name='attributes')
    edit_item = sgqlc.types.Field(String, graphql_name='editItem')
    featured_image = sgqlc.types.Field(String, graphql_name='featuredImage')
    filter_items_list = sgqlc.types.Field(String, graphql_name='filterItemsList')
    insert_into_item = sgqlc.types.Field(String, graphql_name='insertIntoItem')
    items_list = sgqlc.types.Field(String, graphql_name='itemsList')
    items_list_navigation = sgqlc.types.Field(String, graphql_name='itemsListNavigation')
    menu_name = sgqlc.types.Field(String, graphql_name='menuName')
    name = sgqlc.types.Field(String, graphql_name='name')
    new_item = sgqlc.types.Field(String, graphql_name='newItem')
    not_found = sgqlc.types.Field(String, graphql_name='notFound')
    not_found_in_trash = sgqlc.types.Field(String, graphql_name='notFoundInTrash')
    parent_item_colon = sgqlc.types.Field(String, graphql_name='parentItemColon')
    remove_featured_image = sgqlc.types.Field(String, graphql_name='removeFeaturedImage')
    search_items = sgqlc.types.Field(String, graphql_name='searchItems')
    set_featured_image = sgqlc.types.Field(String, graphql_name='setFeaturedImage')
    singular_name = sgqlc.types.Field(String, graphql_name='singularName')
    uploaded_to_this_item = sgqlc.types.Field(String, graphql_name='uploadedToThisItem')
    use_featured_image = sgqlc.types.Field(String, graphql_name='useFeaturedImage')
    view_item = sgqlc.types.Field(String, graphql_name='viewItem')
    view_items = sgqlc.types.Field(String, graphql_name='viewItems')


class ReadingSettings(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('page_for_posts', 'page_on_front', 'posts_per_page', 'show_on_front')
    page_for_posts = sgqlc.types.Field(Int, graphql_name='pageForPosts')
    page_on_front = sgqlc.types.Field(Int, graphql_name='pageOnFront')
    posts_per_page = sgqlc.types.Field(Int, graphql_name='postsPerPage')
    show_on_front = sgqlc.types.Field(String, graphql_name='showOnFront')


class RefreshJwtAuthTokenPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('auth_token', 'client_mutation_id')
    auth_token = sgqlc.types.Field(String, graphql_name='authToken')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class RegisterUserPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'user')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    user = sgqlc.types.Field('User', graphql_name='user')


class ResetUserPasswordPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'user')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    user = sgqlc.types.Field('User', graphql_name='user')


class RestoreCommentPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'comment', 'restored_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    comment = sgqlc.types.Field('Comment', graphql_name='comment')
    restored_id = sgqlc.types.Field(ID, graphql_name='restoredId')


class RootMutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('create_category', 'create_comment', 'create_contract_kind', 'create_event', 'create_events_category', 'create_graphql_document', 'create_graphql_document_group', 'create_job', 'create_jobmode', 'create_media_item', 'create_occupationkind', 'create_organizer', 'create_page', 'create_partner', 'create_post', 'create_post_format', 'create_tag', 'create_user', 'create_venue', 'delete_category', 'delete_comment', 'delete_contract_kind', 'delete_event', 'delete_events_category', 'delete_graphql_document', 'delete_graphql_document_group', 'delete_job', 'delete_jobmode', 'delete_media_item', 'delete_occupationkind', 'delete_organizer', 'delete_page', 'delete_partner', 'delete_post', 'delete_post_format', 'delete_tag', 'delete_user', 'delete_venue', 'increase_count', 'login', 'refresh_jwt_auth_token', 'register_user', 'reset_user_password', 'restore_comment', 'send_password_reset_email', 'update_category', 'update_comment', 'update_contract_kind', 'update_event', 'update_events_category', 'update_graphql_document', 'update_graphql_document_group', 'update_job', 'update_jobmode', 'update_media_item', 'update_occupationkind', 'update_organizer', 'update_page', 'update_partner', 'update_post', 'update_post_format', 'update_settings', 'update_tag', 'update_user', 'update_venue')
    create_category = sgqlc.types.Field(CreateCategoryPayload, graphql_name='createCategory', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateCategoryInput), graphql_name='input', default=None)),
))
    )
    create_comment = sgqlc.types.Field(CreateCommentPayload, graphql_name='createComment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateCommentInput), graphql_name='input', default=None)),
))
    )
    create_contract_kind = sgqlc.types.Field(CreateContractKindPayload, graphql_name='createContractKind', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateContractKindInput), graphql_name='input', default=None)),
))
    )
    create_event = sgqlc.types.Field(CreateEventPayload, graphql_name='createEvent', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateEventInput), graphql_name='input', default=None)),
))
    )
    create_events_category = sgqlc.types.Field(CreateEventsCategoryPayload, graphql_name='createEventsCategory', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateEventsCategoryInput), graphql_name='input', default=None)),
))
    )
    create_graphql_document = sgqlc.types.Field(CreateGraphqlDocumentPayload, graphql_name='createGraphqlDocument', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateGraphqlDocumentInput), graphql_name='input', default=None)),
))
    )
    create_graphql_document_group = sgqlc.types.Field(CreateGraphqlDocumentGroupPayload, graphql_name='createGraphqlDocumentGroup', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateGraphqlDocumentGroupInput), graphql_name='input', default=None)),
))
    )
    create_job = sgqlc.types.Field(CreateJobPayload, graphql_name='createJob', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateJobInput), graphql_name='input', default=None)),
))
    )
    create_jobmode = sgqlc.types.Field(CreateJobmodePayload, graphql_name='createJobmode', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateJobmodeInput), graphql_name='input', default=None)),
))
    )
    create_media_item = sgqlc.types.Field(CreateMediaItemPayload, graphql_name='createMediaItem', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateMediaItemInput), graphql_name='input', default=None)),
))
    )
    create_occupationkind = sgqlc.types.Field(CreateOccupationkindPayload, graphql_name='createOccupationkind', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateOccupationkindInput), graphql_name='input', default=None)),
))
    )
    create_organizer = sgqlc.types.Field(CreateOrganizerPayload, graphql_name='createOrganizer', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateOrganizerInput), graphql_name='input', default=None)),
))
    )
    create_page = sgqlc.types.Field(CreatePagePayload, graphql_name='createPage', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreatePageInput), graphql_name='input', default=None)),
))
    )
    create_partner = sgqlc.types.Field(CreatePartnerPayload, graphql_name='createPartner', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreatePartnerInput), graphql_name='input', default=None)),
))
    )
    create_post = sgqlc.types.Field(CreatePostPayload, graphql_name='createPost', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreatePostInput), graphql_name='input', default=None)),
))
    )
    create_post_format = sgqlc.types.Field(CreatePostFormatPayload, graphql_name='createPostFormat', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreatePostFormatInput), graphql_name='input', default=None)),
))
    )
    create_tag = sgqlc.types.Field(CreateTagPayload, graphql_name='createTag', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateTagInput), graphql_name='input', default=None)),
))
    )
    create_user = sgqlc.types.Field(CreateUserPayload, graphql_name='createUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateUserInput), graphql_name='input', default=None)),
))
    )
    create_venue = sgqlc.types.Field(CreateVenuePayload, graphql_name='createVenue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateVenueInput), graphql_name='input', default=None)),
))
    )
    delete_category = sgqlc.types.Field(DeleteCategoryPayload, graphql_name='deleteCategory', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteCategoryInput), graphql_name='input', default=None)),
))
    )
    delete_comment = sgqlc.types.Field(DeleteCommentPayload, graphql_name='deleteComment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteCommentInput), graphql_name='input', default=None)),
))
    )
    delete_contract_kind = sgqlc.types.Field(DeleteContractKindPayload, graphql_name='deleteContractKind', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteContractKindInput), graphql_name='input', default=None)),
))
    )
    delete_event = sgqlc.types.Field(DeleteEventPayload, graphql_name='deleteEvent', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteEventInput), graphql_name='input', default=None)),
))
    )
    delete_events_category = sgqlc.types.Field(DeleteEventsCategoryPayload, graphql_name='deleteEventsCategory', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteEventsCategoryInput), graphql_name='input', default=None)),
))
    )
    delete_graphql_document = sgqlc.types.Field(DeleteGraphqlDocumentPayload, graphql_name='deleteGraphqlDocument', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteGraphqlDocumentInput), graphql_name='input', default=None)),
))
    )
    delete_graphql_document_group = sgqlc.types.Field(DeleteGraphqlDocumentGroupPayload, graphql_name='deleteGraphqlDocumentGroup', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteGraphqlDocumentGroupInput), graphql_name='input', default=None)),
))
    )
    delete_job = sgqlc.types.Field(DeleteJobPayload, graphql_name='deleteJob', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteJobInput), graphql_name='input', default=None)),
))
    )
    delete_jobmode = sgqlc.types.Field(DeleteJobmodePayload, graphql_name='deleteJobmode', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteJobmodeInput), graphql_name='input', default=None)),
))
    )
    delete_media_item = sgqlc.types.Field(DeleteMediaItemPayload, graphql_name='deleteMediaItem', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteMediaItemInput), graphql_name='input', default=None)),
))
    )
    delete_occupationkind = sgqlc.types.Field(DeleteOccupationkindPayload, graphql_name='deleteOccupationkind', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteOccupationkindInput), graphql_name='input', default=None)),
))
    )
    delete_organizer = sgqlc.types.Field(DeleteOrganizerPayload, graphql_name='deleteOrganizer', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteOrganizerInput), graphql_name='input', default=None)),
))
    )
    delete_page = sgqlc.types.Field(DeletePagePayload, graphql_name='deletePage', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeletePageInput), graphql_name='input', default=None)),
))
    )
    delete_partner = sgqlc.types.Field(DeletePartnerPayload, graphql_name='deletePartner', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeletePartnerInput), graphql_name='input', default=None)),
))
    )
    delete_post = sgqlc.types.Field(DeletePostPayload, graphql_name='deletePost', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeletePostInput), graphql_name='input', default=None)),
))
    )
    delete_post_format = sgqlc.types.Field(DeletePostFormatPayload, graphql_name='deletePostFormat', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeletePostFormatInput), graphql_name='input', default=None)),
))
    )
    delete_tag = sgqlc.types.Field(DeleteTagPayload, graphql_name='deleteTag', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteTagInput), graphql_name='input', default=None)),
))
    )
    delete_user = sgqlc.types.Field(DeleteUserPayload, graphql_name='deleteUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteUserInput), graphql_name='input', default=None)),
))
    )
    delete_venue = sgqlc.types.Field(DeleteVenuePayload, graphql_name='deleteVenue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteVenueInput), graphql_name='input', default=None)),
))
    )
    increase_count = sgqlc.types.Field(Int, graphql_name='increaseCount', args=sgqlc.types.ArgDict((
        ('count', sgqlc.types.Arg(Int, graphql_name='count', default=None)),
))
    )
    login = sgqlc.types.Field(LoginPayload, graphql_name='login', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(LoginInput), graphql_name='input', default=None)),
))
    )
    refresh_jwt_auth_token = sgqlc.types.Field(RefreshJwtAuthTokenPayload, graphql_name='refreshJwtAuthToken', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RefreshJwtAuthTokenInput), graphql_name='input', default=None)),
))
    )
    register_user = sgqlc.types.Field(RegisterUserPayload, graphql_name='registerUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RegisterUserInput), graphql_name='input', default=None)),
))
    )
    reset_user_password = sgqlc.types.Field(ResetUserPasswordPayload, graphql_name='resetUserPassword', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ResetUserPasswordInput), graphql_name='input', default=None)),
))
    )
    restore_comment = sgqlc.types.Field(RestoreCommentPayload, graphql_name='restoreComment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RestoreCommentInput), graphql_name='input', default=None)),
))
    )
    send_password_reset_email = sgqlc.types.Field('SendPasswordResetEmailPayload', graphql_name='sendPasswordResetEmail', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SendPasswordResetEmailInput), graphql_name='input', default=None)),
))
    )
    update_category = sgqlc.types.Field('UpdateCategoryPayload', graphql_name='updateCategory', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateCategoryInput), graphql_name='input', default=None)),
))
    )
    update_comment = sgqlc.types.Field('UpdateCommentPayload', graphql_name='updateComment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateCommentInput), graphql_name='input', default=None)),
))
    )
    update_contract_kind = sgqlc.types.Field('UpdateContractKindPayload', graphql_name='updateContractKind', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateContractKindInput), graphql_name='input', default=None)),
))
    )
    update_event = sgqlc.types.Field('UpdateEventPayload', graphql_name='updateEvent', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEventInput), graphql_name='input', default=None)),
))
    )
    update_events_category = sgqlc.types.Field('UpdateEventsCategoryPayload', graphql_name='updateEventsCategory', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEventsCategoryInput), graphql_name='input', default=None)),
))
    )
    update_graphql_document = sgqlc.types.Field('UpdateGraphqlDocumentPayload', graphql_name='updateGraphqlDocument', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateGraphqlDocumentInput), graphql_name='input', default=None)),
))
    )
    update_graphql_document_group = sgqlc.types.Field('UpdateGraphqlDocumentGroupPayload', graphql_name='updateGraphqlDocumentGroup', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateGraphqlDocumentGroupInput), graphql_name='input', default=None)),
))
    )
    update_job = sgqlc.types.Field('UpdateJobPayload', graphql_name='updateJob', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateJobInput), graphql_name='input', default=None)),
))
    )
    update_jobmode = sgqlc.types.Field('UpdateJobmodePayload', graphql_name='updateJobmode', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateJobmodeInput), graphql_name='input', default=None)),
))
    )
    update_media_item = sgqlc.types.Field('UpdateMediaItemPayload', graphql_name='updateMediaItem', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateMediaItemInput), graphql_name='input', default=None)),
))
    )
    update_occupationkind = sgqlc.types.Field('UpdateOccupationkindPayload', graphql_name='updateOccupationkind', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateOccupationkindInput), graphql_name='input', default=None)),
))
    )
    update_organizer = sgqlc.types.Field('UpdateOrganizerPayload', graphql_name='updateOrganizer', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateOrganizerInput), graphql_name='input', default=None)),
))
    )
    update_page = sgqlc.types.Field('UpdatePagePayload', graphql_name='updatePage', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdatePageInput), graphql_name='input', default=None)),
))
    )
    update_partner = sgqlc.types.Field('UpdatePartnerPayload', graphql_name='updatePartner', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdatePartnerInput), graphql_name='input', default=None)),
))
    )
    update_post = sgqlc.types.Field('UpdatePostPayload', graphql_name='updatePost', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdatePostInput), graphql_name='input', default=None)),
))
    )
    update_post_format = sgqlc.types.Field('UpdatePostFormatPayload', graphql_name='updatePostFormat', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdatePostFormatInput), graphql_name='input', default=None)),
))
    )
    update_settings = sgqlc.types.Field('UpdateSettingsPayload', graphql_name='updateSettings', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateSettingsInput), graphql_name='input', default=None)),
))
    )
    update_tag = sgqlc.types.Field('UpdateTagPayload', graphql_name='updateTag', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateTagInput), graphql_name='input', default=None)),
))
    )
    update_user = sgqlc.types.Field('UpdateUserPayload', graphql_name='updateUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateUserInput), graphql_name='input', default=None)),
))
    )
    update_venue = sgqlc.types.Field('UpdateVenuePayload', graphql_name='updateVenue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateVenueInput), graphql_name='input', default=None)),
))
    )


class RootQuery(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('all_settings', 'categories', 'category', 'comment', 'comments', 'content_node', 'content_nodes', 'content_type', 'content_types', 'contract_kind', 'contractkinds', 'discussion_settings', 'event', 'events', 'events_categories', 'events_category', 'general_settings', 'graphql_document', 'graphql_document_group', 'graphql_document_groups', 'graphql_documents', 'job', 'jobmode', 'jobmodes', 'jobs', 'media_item', 'media_items', 'menu', 'menu_item', 'menu_items', 'menus', 'node', 'node_by_uri', 'occupationkind', 'occupationkinds', 'organizer', 'organizers', 'page', 'pages', 'partner', 'partners', 'plugin', 'plugins', 'post', 'post_format', 'post_formats', 'posts', 'reading_settings', 'registered_scripts', 'registered_stylesheets', 'revisions', 'tag', 'tags', 'taxonomies', 'taxonomy', 'term_node', 'terms', 'theme', 'themes', 'user', 'user_role', 'user_roles', 'users', 'venue', 'venues', 'viewer', 'writing_settings')
    all_settings = sgqlc.types.Field('Settings', graphql_name='allSettings')
    categories = sgqlc.types.Field('RootQueryToCategoryConnection', graphql_name='categories', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(RootQueryToCategoryConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    category = sgqlc.types.Field('Category', graphql_name='category', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('id_type', sgqlc.types.Arg(CategoryIdType, graphql_name='idType', default=None)),
))
    )
    comment = sgqlc.types.Field('Comment', graphql_name='comment', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('id_type', sgqlc.types.Arg(CommentNodeIdTypeEnum, graphql_name='idType', default=None)),
))
    )
    comments = sgqlc.types.Field('RootQueryToCommentConnection', graphql_name='comments', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(RootQueryToCommentConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    content_node = sgqlc.types.Field(ContentNode, graphql_name='contentNode', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('id_type', sgqlc.types.Arg(ContentNodeIdTypeEnum, graphql_name='idType', default=None)),
        ('content_type', sgqlc.types.Arg(ContentTypeEnum, graphql_name='contentType', default=None)),
        ('as_preview', sgqlc.types.Arg(Boolean, graphql_name='asPreview', default=None)),
))
    )
    content_nodes = sgqlc.types.Field('RootQueryToContentNodeConnection', graphql_name='contentNodes', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(RootQueryToContentNodeConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    content_type = sgqlc.types.Field('ContentType', graphql_name='contentType', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('id_type', sgqlc.types.Arg(ContentTypeIdTypeEnum, graphql_name='idType', default=None)),
))
    )
    content_types = sgqlc.types.Field('RootQueryToContentTypeConnection', graphql_name='contentTypes', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    contract_kind = sgqlc.types.Field('ContractKind', graphql_name='contractKind', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('id_type', sgqlc.types.Arg(ContractKindIdType, graphql_name='idType', default=None)),
))
    )
    contractkinds = sgqlc.types.Field('RootQueryToContractKindConnection', graphql_name='contractkinds', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(RootQueryToContractKindConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    discussion_settings = sgqlc.types.Field(DiscussionSettings, graphql_name='discussionSettings')
    event = sgqlc.types.Field('Event', graphql_name='event', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('id_type', sgqlc.types.Arg(EventIdType, graphql_name='idType', default=None)),
        ('as_preview', sgqlc.types.Arg(Boolean, graphql_name='asPreview', default=None)),
))
    )
    events = sgqlc.types.Field('RootQueryToEventConnection', graphql_name='events', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(RootQueryToEventConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    events_categories = sgqlc.types.Field('RootQueryToEventsCategoryConnection', graphql_name='eventsCategories', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(RootQueryToEventsCategoryConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    events_category = sgqlc.types.Field('EventsCategory', graphql_name='eventsCategory', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('id_type', sgqlc.types.Arg(EventsCategoryIdType, graphql_name='idType', default=None)),
))
    )
    general_settings = sgqlc.types.Field(GeneralSettings, graphql_name='generalSettings')
    graphql_document = sgqlc.types.Field('GraphqlDocument', graphql_name='graphqlDocument', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('id_type', sgqlc.types.Arg(GraphqlDocumentIdType, graphql_name='idType', default=None)),
        ('as_preview', sgqlc.types.Arg(Boolean, graphql_name='asPreview', default=None)),
))
    )
    graphql_document_group = sgqlc.types.Field('GraphqlDocumentGroup', graphql_name='graphqlDocumentGroup', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('id_type', sgqlc.types.Arg(GraphqlDocumentGroupIdType, graphql_name='idType', default=None)),
))
    )
    graphql_document_groups = sgqlc.types.Field('RootQueryToGraphqlDocumentGroupConnection', graphql_name='graphqlDocumentGroups', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(RootQueryToGraphqlDocumentGroupConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    graphql_documents = sgqlc.types.Field('RootQueryToGraphqlDocumentConnection', graphql_name='graphqlDocuments', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(RootQueryToGraphqlDocumentConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    job = sgqlc.types.Field('Job', graphql_name='job', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('id_type', sgqlc.types.Arg(JobIdType, graphql_name='idType', default=None)),
        ('as_preview', sgqlc.types.Arg(Boolean, graphql_name='asPreview', default=None)),
))
    )
    jobmode = sgqlc.types.Field('Jobmode', graphql_name='jobmode', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('id_type', sgqlc.types.Arg(JobmodeIdType, graphql_name='idType', default=None)),
))
    )
    jobmodes = sgqlc.types.Field('RootQueryToJobmodeConnection', graphql_name='jobmodes', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(RootQueryToJobmodeConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    jobs = sgqlc.types.Field('RootQueryToJobConnection', graphql_name='jobs', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(RootQueryToJobConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    media_item = sgqlc.types.Field('MediaItem', graphql_name='mediaItem', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('id_type', sgqlc.types.Arg(MediaItemIdType, graphql_name='idType', default=None)),
        ('as_preview', sgqlc.types.Arg(Boolean, graphql_name='asPreview', default=None)),
))
    )
    media_items = sgqlc.types.Field('RootQueryToMediaItemConnection', graphql_name='mediaItems', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(RootQueryToMediaItemConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    menu = sgqlc.types.Field('Menu', graphql_name='menu', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('id_type', sgqlc.types.Arg(MenuNodeIdTypeEnum, graphql_name='idType', default=None)),
))
    )
    menu_item = sgqlc.types.Field('MenuItem', graphql_name='menuItem', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('id_type', sgqlc.types.Arg(MenuItemNodeIdTypeEnum, graphql_name='idType', default=None)),
))
    )
    menu_items = sgqlc.types.Field('RootQueryToMenuItemConnection', graphql_name='menuItems', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(RootQueryToMenuItemConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    menus = sgqlc.types.Field('RootQueryToMenuConnection', graphql_name='menus', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(RootQueryToMenuConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    node = sgqlc.types.Field(Node, graphql_name='node', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(ID, graphql_name='id', default=None)),
))
    )
    node_by_uri = sgqlc.types.Field(UniformResourceIdentifiable, graphql_name='nodeByUri', args=sgqlc.types.ArgDict((
        ('uri', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='uri', default=None)),
))
    )
    occupationkind = sgqlc.types.Field('Occupationkind', graphql_name='occupationkind', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('id_type', sgqlc.types.Arg(OccupationkindIdType, graphql_name='idType', default=None)),
))
    )
    occupationkinds = sgqlc.types.Field('RootQueryToOccupationkindConnection', graphql_name='occupationkinds', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(RootQueryToOccupationkindConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    organizer = sgqlc.types.Field('Organizer', graphql_name='organizer', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('id_type', sgqlc.types.Arg(OrganizerIdType, graphql_name='idType', default=None)),
        ('as_preview', sgqlc.types.Arg(Boolean, graphql_name='asPreview', default=None)),
))
    )
    organizers = sgqlc.types.Field('RootQueryToOrganizerConnection', graphql_name='organizers', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(RootQueryToOrganizerConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    page = sgqlc.types.Field('Page', graphql_name='page', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('id_type', sgqlc.types.Arg(PageIdType, graphql_name='idType', default=None)),
        ('as_preview', sgqlc.types.Arg(Boolean, graphql_name='asPreview', default=None)),
))
    )
    pages = sgqlc.types.Field('RootQueryToPageConnection', graphql_name='pages', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(RootQueryToPageConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    partner = sgqlc.types.Field('Partner', graphql_name='partner', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('id_type', sgqlc.types.Arg(PartnerIdType, graphql_name='idType', default=None)),
        ('as_preview', sgqlc.types.Arg(Boolean, graphql_name='asPreview', default=None)),
))
    )
    partners = sgqlc.types.Field('RootQueryToPartnerConnection', graphql_name='partners', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(RootQueryToPartnerConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    plugin = sgqlc.types.Field('Plugin', graphql_name='plugin', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    plugins = sgqlc.types.Field('RootQueryToPluginConnection', graphql_name='plugins', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(RootQueryToPluginConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    post = sgqlc.types.Field('Post', graphql_name='post', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('id_type', sgqlc.types.Arg(PostIdType, graphql_name='idType', default=None)),
        ('as_preview', sgqlc.types.Arg(Boolean, graphql_name='asPreview', default=None)),
))
    )
    post_format = sgqlc.types.Field('PostFormat', graphql_name='postFormat', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('id_type', sgqlc.types.Arg(PostFormatIdType, graphql_name='idType', default=None)),
))
    )
    post_formats = sgqlc.types.Field('RootQueryToPostFormatConnection', graphql_name='postFormats', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(RootQueryToPostFormatConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    posts = sgqlc.types.Field('RootQueryToPostConnection', graphql_name='posts', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(RootQueryToPostConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    reading_settings = sgqlc.types.Field(ReadingSettings, graphql_name='readingSettings')
    registered_scripts = sgqlc.types.Field('RootQueryToEnqueuedScriptConnection', graphql_name='registeredScripts', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    registered_stylesheets = sgqlc.types.Field('RootQueryToEnqueuedStylesheetConnection', graphql_name='registeredStylesheets', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    revisions = sgqlc.types.Field('RootQueryToRevisionsConnection', graphql_name='revisions', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(RootQueryToRevisionsConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    tag = sgqlc.types.Field('Tag', graphql_name='tag', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('id_type', sgqlc.types.Arg(TagIdType, graphql_name='idType', default=None)),
))
    )
    tags = sgqlc.types.Field('RootQueryToTagConnection', graphql_name='tags', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(RootQueryToTagConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    taxonomies = sgqlc.types.Field('RootQueryToTaxonomyConnection', graphql_name='taxonomies', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    taxonomy = sgqlc.types.Field('Taxonomy', graphql_name='taxonomy', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('id_type', sgqlc.types.Arg(TaxonomyIdTypeEnum, graphql_name='idType', default=None)),
))
    )
    term_node = sgqlc.types.Field(TermNode, graphql_name='termNode', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('id_type', sgqlc.types.Arg(TermNodeIdTypeEnum, graphql_name='idType', default=None)),
        ('taxonomy', sgqlc.types.Arg(TaxonomyEnum, graphql_name='taxonomy', default=None)),
))
    )
    terms = sgqlc.types.Field('RootQueryToTermNodeConnection', graphql_name='terms', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(RootQueryToTermNodeConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    theme = sgqlc.types.Field('Theme', graphql_name='theme', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    themes = sgqlc.types.Field('RootQueryToThemeConnection', graphql_name='themes', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    user = sgqlc.types.Field('User', graphql_name='user', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('id_type', sgqlc.types.Arg(UserNodeIdTypeEnum, graphql_name='idType', default=None)),
))
    )
    user_role = sgqlc.types.Field('UserRole', graphql_name='userRole', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    user_roles = sgqlc.types.Field('RootQueryToUserRoleConnection', graphql_name='userRoles', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    users = sgqlc.types.Field('RootQueryToUserConnection', graphql_name='users', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(RootQueryToUserConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    venue = sgqlc.types.Field('Venue', graphql_name='venue', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
        ('id_type', sgqlc.types.Arg(VenueIdType, graphql_name='idType', default=None)),
        ('as_preview', sgqlc.types.Arg(Boolean, graphql_name='asPreview', default=None)),
))
    )
    venues = sgqlc.types.Field('RootQueryToVenueConnection', graphql_name='venues', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(RootQueryToVenueConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    viewer = sgqlc.types.Field('User', graphql_name='viewer')
    writing_settings = sgqlc.types.Field('WritingSettings', graphql_name='writingSettings')


class SendPasswordResetEmailPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'success')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class Settings(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('discussion_settings_default_comment_status', 'discussion_settings_default_ping_status', 'general_settings_date_format', 'general_settings_description', 'general_settings_email', 'general_settings_language', 'general_settings_start_of_week', 'general_settings_time_format', 'general_settings_timezone', 'general_settings_title', 'general_settings_url', 'reading_settings_page_for_posts', 'reading_settings_page_on_front', 'reading_settings_posts_per_page', 'reading_settings_show_on_front', 'writing_settings_default_category', 'writing_settings_default_post_format', 'writing_settings_use_smilies')
    discussion_settings_default_comment_status = sgqlc.types.Field(String, graphql_name='discussionSettingsDefaultCommentStatus')
    discussion_settings_default_ping_status = sgqlc.types.Field(String, graphql_name='discussionSettingsDefaultPingStatus')
    general_settings_date_format = sgqlc.types.Field(String, graphql_name='generalSettingsDateFormat')
    general_settings_description = sgqlc.types.Field(String, graphql_name='generalSettingsDescription')
    general_settings_email = sgqlc.types.Field(String, graphql_name='generalSettingsEmail')
    general_settings_language = sgqlc.types.Field(String, graphql_name='generalSettingsLanguage')
    general_settings_start_of_week = sgqlc.types.Field(Int, graphql_name='generalSettingsStartOfWeek')
    general_settings_time_format = sgqlc.types.Field(String, graphql_name='generalSettingsTimeFormat')
    general_settings_timezone = sgqlc.types.Field(String, graphql_name='generalSettingsTimezone')
    general_settings_title = sgqlc.types.Field(String, graphql_name='generalSettingsTitle')
    general_settings_url = sgqlc.types.Field(String, graphql_name='generalSettingsUrl')
    reading_settings_page_for_posts = sgqlc.types.Field(Int, graphql_name='readingSettingsPageForPosts')
    reading_settings_page_on_front = sgqlc.types.Field(Int, graphql_name='readingSettingsPageOnFront')
    reading_settings_posts_per_page = sgqlc.types.Field(Int, graphql_name='readingSettingsPostsPerPage')
    reading_settings_show_on_front = sgqlc.types.Field(String, graphql_name='readingSettingsShowOnFront')
    writing_settings_default_category = sgqlc.types.Field(Int, graphql_name='writingSettingsDefaultCategory')
    writing_settings_default_post_format = sgqlc.types.Field(String, graphql_name='writingSettingsDefaultPostFormat')
    writing_settings_use_smilies = sgqlc.types.Field(Boolean, graphql_name='writingSettingsUseSmilies')


class UpdateCategoryPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('category', 'client_mutation_id')
    category = sgqlc.types.Field('Category', graphql_name='category')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UpdateCommentPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'comment', 'success')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    comment = sgqlc.types.Field('Comment', graphql_name='comment')
    success = sgqlc.types.Field(Boolean, graphql_name='success')


class UpdateContractKindPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'contract_kind')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    contract_kind = sgqlc.types.Field('ContractKind', graphql_name='contractKind')


class UpdateEventPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('event', 'client_mutation_id')
    event = sgqlc.types.Field('Event', graphql_name='event')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UpdateEventsCategoryPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('events_category', 'client_mutation_id')
    events_category = sgqlc.types.Field('EventsCategory', graphql_name='eventsCategory')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UpdateGraphqlDocumentGroupPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'graphql_document_group')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    graphql_document_group = sgqlc.types.Field('GraphqlDocumentGroup', graphql_name='graphqlDocumentGroup')


class UpdateGraphqlDocumentPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'graphql_document')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    graphql_document = sgqlc.types.Field('GraphqlDocument', graphql_name='graphqlDocument')


class UpdateJobPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'job')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    job = sgqlc.types.Field('Job', graphql_name='job')


class UpdateJobmodePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'jobmode')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    jobmode = sgqlc.types.Field('Jobmode', graphql_name='jobmode')


class UpdateMediaItemPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'media_item')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    media_item = sgqlc.types.Field('MediaItem', graphql_name='mediaItem')


class UpdateOccupationkindPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'occupationkind')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    occupationkind = sgqlc.types.Field('Occupationkind', graphql_name='occupationkind')


class UpdateOrganizerPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('organizer', 'client_mutation_id')
    organizer = sgqlc.types.Field('Organizer', graphql_name='organizer')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UpdatePagePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'page')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    page = sgqlc.types.Field('Page', graphql_name='page')


class UpdatePartnerPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'partner')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    partner = sgqlc.types.Field('Partner', graphql_name='partner')


class UpdatePostFormatPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'post_format')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    post_format = sgqlc.types.Field('PostFormat', graphql_name='postFormat')


class UpdatePostPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'post')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    post = sgqlc.types.Field('Post', graphql_name='post')


class UpdateSettingsPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('all_settings', 'client_mutation_id', 'discussion_settings', 'general_settings', 'reading_settings', 'writing_settings')
    all_settings = sgqlc.types.Field(Settings, graphql_name='allSettings')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    discussion_settings = sgqlc.types.Field(DiscussionSettings, graphql_name='discussionSettings')
    general_settings = sgqlc.types.Field(GeneralSettings, graphql_name='generalSettings')
    reading_settings = sgqlc.types.Field(ReadingSettings, graphql_name='readingSettings')
    writing_settings = sgqlc.types.Field('WritingSettings', graphql_name='writingSettings')


class UpdateTagPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'tag')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    tag = sgqlc.types.Field('Tag', graphql_name='tag')


class UpdateUserPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'user')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    user = sgqlc.types.Field('User', graphql_name='user')


class UpdateVenuePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('venue', 'client_mutation_id')
    venue = sgqlc.types.Field('Venue', graphql_name='venue')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class VenueLinkedData(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('address', 'description', 'name', 'same_as', 'telephone', 'type', 'url')
    address = sgqlc.types.Field(AddressLinkedData, graphql_name='address')
    description = sgqlc.types.Field(String, graphql_name='description')
    name = sgqlc.types.Field(String, graphql_name='name')
    same_as = sgqlc.types.Field(String, graphql_name='sameAs')
    telephone = sgqlc.types.Field(String, graphql_name='telephone')
    type = sgqlc.types.Field(String, graphql_name='type')
    url = sgqlc.types.Field(String, graphql_name='url')


class WritingSettings(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('default_category', 'default_post_format', 'use_smilies')
    default_category = sgqlc.types.Field(Int, graphql_name='defaultCategory')
    default_post_format = sgqlc.types.Field(String, graphql_name='defaultPostFormat')
    use_smilies = sgqlc.types.Field(Boolean, graphql_name='useSmilies')


class AcfMediaItemConnectionEdge(sgqlc.types.Type, OneToOneConnection, Edge, MediaItemConnectionEdge):
    __schema__ = schema
    __field_names__ = ()


class Category(sgqlc.types.Type, Node, TermNode, UniformResourceIdentifiable, DatabaseIdentifier, HierarchicalTermNode, HierarchicalNode, MenuItemLinkable):
    __schema__ = schema
    __field_names__ = ('ancestors', 'children', 'content_nodes', 'parent', 'posts', 'taxonomy')
    ancestors = sgqlc.types.Field('CategoryToAncestorsCategoryConnection', graphql_name='ancestors', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    children = sgqlc.types.Field('CategoryToCategoryConnection', graphql_name='children', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(CategoryToCategoryConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    content_nodes = sgqlc.types.Field('CategoryToContentNodeConnection', graphql_name='contentNodes', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(CategoryToContentNodeConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    parent = sgqlc.types.Field('CategoryToParentCategoryConnectionEdge', graphql_name='parent')
    posts = sgqlc.types.Field('CategoryToPostConnection', graphql_name='posts', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(CategoryToPostConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    taxonomy = sgqlc.types.Field('CategoryToTaxonomyConnectionEdge', graphql_name='taxonomy')


class CategoryToAncestorsCategoryConnection(sgqlc.types.relay.Connection, CategoryConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class CategoryToAncestorsCategoryConnectionEdge(sgqlc.types.Type, CategoryConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class CategoryToAncestorsCategoryConnectionPageInfo(sgqlc.types.Type, CategoryConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class CategoryToCategoryConnection(sgqlc.types.relay.Connection, CategoryConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class CategoryToCategoryConnectionEdge(sgqlc.types.Type, CategoryConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class CategoryToCategoryConnectionPageInfo(sgqlc.types.Type, CategoryConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class CategoryToContentNodeConnection(sgqlc.types.relay.Connection, ContentNodeConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class CategoryToContentNodeConnectionEdge(sgqlc.types.Type, ContentNodeConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class CategoryToContentNodeConnectionPageInfo(sgqlc.types.Type, ContentNodeConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class CategoryToParentCategoryConnectionEdge(sgqlc.types.Type, OneToOneConnection, Edge, CategoryConnectionEdge):
    __schema__ = schema
    __field_names__ = ()


class CategoryToPostConnection(sgqlc.types.relay.Connection, PostConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class CategoryToPostConnectionEdge(sgqlc.types.Type, PostConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class CategoryToPostConnectionPageInfo(sgqlc.types.Type, PostConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class CategoryToTaxonomyConnectionEdge(sgqlc.types.Type, OneToOneConnection, Edge, TaxonomyConnectionEdge):
    __schema__ = schema
    __field_names__ = ()


class Comment(sgqlc.types.Type, Node, DatabaseIdentifier, UniformResourceIdentifiable):
    __schema__ = schema
    __field_names__ = ('agent', 'author', 'commented_on', 'content', 'date', 'date_gmt', 'is_restricted', 'karma', 'link', 'parent', 'parent_database_id', 'parent_id', 'replies', 'status', 'type')
    agent = sgqlc.types.Field(String, graphql_name='agent')
    author = sgqlc.types.Field('CommentToCommenterConnectionEdge', graphql_name='author')
    commented_on = sgqlc.types.Field('CommentToContentNodeConnectionEdge', graphql_name='commentedOn')
    content = sgqlc.types.Field(String, graphql_name='content', args=sgqlc.types.ArgDict((
        ('format', sgqlc.types.Arg(PostObjectFieldFormatEnum, graphql_name='format', default=None)),
))
    )
    date = sgqlc.types.Field(String, graphql_name='date')
    date_gmt = sgqlc.types.Field(String, graphql_name='dateGmt')
    is_restricted = sgqlc.types.Field(Boolean, graphql_name='isRestricted')
    karma = sgqlc.types.Field(Int, graphql_name='karma')
    link = sgqlc.types.Field(String, graphql_name='link')
    parent = sgqlc.types.Field('CommentToParentCommentConnectionEdge', graphql_name='parent', args=sgqlc.types.ArgDict((
        ('where', sgqlc.types.Arg(CommentToParentCommentConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    parent_database_id = sgqlc.types.Field(Int, graphql_name='parentDatabaseId')
    parent_id = sgqlc.types.Field(ID, graphql_name='parentId')
    replies = sgqlc.types.Field('CommentToCommentConnection', graphql_name='replies', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(CommentToCommentConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    status = sgqlc.types.Field(CommentStatusEnum, graphql_name='status')
    type = sgqlc.types.Field(String, graphql_name='type')


class CommentAuthor(sgqlc.types.Type, Node, Commenter, DatabaseIdentifier):
    __schema__ = schema
    __field_names__ = ()


class CommentToCommentConnection(sgqlc.types.relay.Connection, CommentConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class CommentToCommentConnectionEdge(sgqlc.types.Type, CommentConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class CommentToCommentConnectionPageInfo(sgqlc.types.Type, CommentConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class CommentToCommenterConnectionEdge(sgqlc.types.Type, OneToOneConnection, Edge, CommenterConnectionEdge):
    __schema__ = schema
    __field_names__ = ('email', 'ip_address', 'name', 'url')
    email = sgqlc.types.Field(String, graphql_name='email')
    ip_address = sgqlc.types.Field(String, graphql_name='ipAddress')
    name = sgqlc.types.Field(String, graphql_name='name')
    url = sgqlc.types.Field(String, graphql_name='url')


class CommentToContentNodeConnectionEdge(sgqlc.types.Type, OneToOneConnection, Edge, ContentNodeConnectionEdge):
    __schema__ = schema
    __field_names__ = ()


class CommentToParentCommentConnectionEdge(sgqlc.types.Type, OneToOneConnection, Edge, CommentConnectionEdge):
    __schema__ = schema
    __field_names__ = ()


class ContentNodeToContentTypeConnectionEdge(sgqlc.types.Type, OneToOneConnection, Edge, ContentTypeConnectionEdge):
    __schema__ = schema
    __field_names__ = ()


class ContentNodeToEditLastConnectionEdge(sgqlc.types.Type, OneToOneConnection, Edge, UserConnectionEdge):
    __schema__ = schema
    __field_names__ = ()


class ContentNodeToEditLockConnectionEdge(sgqlc.types.Type, OneToOneConnection, Edge, UserConnectionEdge):
    __schema__ = schema
    __field_names__ = ('lock_timestamp',)
    lock_timestamp = sgqlc.types.Field(String, graphql_name='lockTimestamp')


class ContentNodeToEnqueuedScriptConnection(sgqlc.types.relay.Connection, EnqueuedScriptConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class ContentNodeToEnqueuedScriptConnectionEdge(sgqlc.types.Type, EnqueuedScriptConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class ContentNodeToEnqueuedScriptConnectionPageInfo(sgqlc.types.Type, EnqueuedScriptConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class ContentNodeToEnqueuedStylesheetConnection(sgqlc.types.relay.Connection, EnqueuedStylesheetConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class ContentNodeToEnqueuedStylesheetConnectionEdge(sgqlc.types.Type, EnqueuedStylesheetConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class ContentNodeToEnqueuedStylesheetConnectionPageInfo(sgqlc.types.Type, EnqueuedStylesheetConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class ContentType(sgqlc.types.Type, Node, UniformResourceIdentifiable):
    __schema__ = schema
    __field_names__ = ('can_export', 'connected_taxonomies', 'content_nodes', 'delete_with_user', 'description', 'exclude_from_search', 'graphql_plural_name', 'graphql_single_name', 'has_archive', 'hierarchical', 'is_restricted', 'label', 'labels', 'menu_icon', 'menu_position', 'name', 'public', 'publicly_queryable', 'rest_base', 'rest_controller_class', 'show_in_admin_bar', 'show_in_graphql', 'show_in_menu', 'show_in_nav_menus', 'show_in_rest', 'show_ui')
    can_export = sgqlc.types.Field(Boolean, graphql_name='canExport')
    connected_taxonomies = sgqlc.types.Field('ContentTypeToTaxonomyConnection', graphql_name='connectedTaxonomies', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    content_nodes = sgqlc.types.Field('ContentTypeToContentNodeConnection', graphql_name='contentNodes', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(ContentTypeToContentNodeConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    delete_with_user = sgqlc.types.Field(Boolean, graphql_name='deleteWithUser')
    description = sgqlc.types.Field(String, graphql_name='description')
    exclude_from_search = sgqlc.types.Field(Boolean, graphql_name='excludeFromSearch')
    graphql_plural_name = sgqlc.types.Field(String, graphql_name='graphqlPluralName')
    graphql_single_name = sgqlc.types.Field(String, graphql_name='graphqlSingleName')
    has_archive = sgqlc.types.Field(Boolean, graphql_name='hasArchive')
    hierarchical = sgqlc.types.Field(Boolean, graphql_name='hierarchical')
    is_restricted = sgqlc.types.Field(Boolean, graphql_name='isRestricted')
    label = sgqlc.types.Field(String, graphql_name='label')
    labels = sgqlc.types.Field(PostTypeLabelDetails, graphql_name='labels')
    menu_icon = sgqlc.types.Field(String, graphql_name='menuIcon')
    menu_position = sgqlc.types.Field(Int, graphql_name='menuPosition')
    name = sgqlc.types.Field(String, graphql_name='name')
    public = sgqlc.types.Field(Boolean, graphql_name='public')
    publicly_queryable = sgqlc.types.Field(Boolean, graphql_name='publiclyQueryable')
    rest_base = sgqlc.types.Field(String, graphql_name='restBase')
    rest_controller_class = sgqlc.types.Field(String, graphql_name='restControllerClass')
    show_in_admin_bar = sgqlc.types.Field(Boolean, graphql_name='showInAdminBar')
    show_in_graphql = sgqlc.types.Field(Boolean, graphql_name='showInGraphql')
    show_in_menu = sgqlc.types.Field(Boolean, graphql_name='showInMenu')
    show_in_nav_menus = sgqlc.types.Field(Boolean, graphql_name='showInNavMenus')
    show_in_rest = sgqlc.types.Field(Boolean, graphql_name='showInRest')
    show_ui = sgqlc.types.Field(Boolean, graphql_name='showUi')


class ContentTypeToContentNodeConnection(sgqlc.types.relay.Connection, ContentNodeConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class ContentTypeToContentNodeConnectionEdge(sgqlc.types.Type, ContentNodeConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class ContentTypeToContentNodeConnectionPageInfo(sgqlc.types.Type, ContentNodeConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class ContentTypeToTaxonomyConnection(sgqlc.types.relay.Connection, TaxonomyConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class ContentTypeToTaxonomyConnectionEdge(sgqlc.types.Type, TaxonomyConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class ContentTypeToTaxonomyConnectionPageInfo(sgqlc.types.Type, TaxonomyConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class ContractKind(sgqlc.types.Type, Node, TermNode, UniformResourceIdentifiable, DatabaseIdentifier, HierarchicalTermNode, HierarchicalNode, MenuItemLinkable):
    __schema__ = schema
    __field_names__ = ('ancestors', 'children', 'content_nodes', 'jobs', 'parent', 'taxonomy')
    ancestors = sgqlc.types.Field('ContractKindToAncestorsContractKindConnection', graphql_name='ancestors', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    children = sgqlc.types.Field('ContractKindToContractKindConnection', graphql_name='children', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(ContractKindToContractKindConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    content_nodes = sgqlc.types.Field('ContractKindToContentNodeConnection', graphql_name='contentNodes', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(ContractKindToContentNodeConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    jobs = sgqlc.types.Field('ContractKindToJobConnection', graphql_name='jobs', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(ContractKindToJobConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    parent = sgqlc.types.Field('ContractKindToParentContractKindConnectionEdge', graphql_name='parent')
    taxonomy = sgqlc.types.Field('ContractKindToTaxonomyConnectionEdge', graphql_name='taxonomy')


class ContractKindToAncestorsContractKindConnection(sgqlc.types.relay.Connection, ContractKindConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class ContractKindToAncestorsContractKindConnectionEdge(sgqlc.types.Type, ContractKindConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class ContractKindToAncestorsContractKindConnectionPageInfo(sgqlc.types.Type, ContractKindConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class ContractKindToContentNodeConnection(sgqlc.types.relay.Connection, ContentNodeConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class ContractKindToContentNodeConnectionEdge(sgqlc.types.Type, ContentNodeConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class ContractKindToContentNodeConnectionPageInfo(sgqlc.types.Type, ContentNodeConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class ContractKindToContractKindConnection(sgqlc.types.relay.Connection, ContractKindConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class ContractKindToContractKindConnectionEdge(sgqlc.types.Type, ContractKindConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class ContractKindToContractKindConnectionPageInfo(sgqlc.types.Type, ContractKindConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class ContractKindToJobConnection(sgqlc.types.relay.Connection, JobConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class ContractKindToJobConnectionEdge(sgqlc.types.Type, JobConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class ContractKindToJobConnectionPageInfo(sgqlc.types.Type, JobConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class ContractKindToParentContractKindConnectionEdge(sgqlc.types.Type, OneToOneConnection, Edge, ContractKindConnectionEdge):
    __schema__ = schema
    __field_names__ = ()


class ContractKindToTaxonomyConnectionEdge(sgqlc.types.Type, OneToOneConnection, Edge, TaxonomyConnectionEdge):
    __schema__ = schema
    __field_names__ = ()


class DefaultTemplate(sgqlc.types.Type, ContentTemplate):
    __schema__ = schema
    __field_names__ = ()


class EnqueuedScript(sgqlc.types.Type, Node, EnqueuedAsset):
    __schema__ = schema
    __field_names__ = ('extra_data', 'strategy')
    extra_data = sgqlc.types.Field(String, graphql_name='extraData')
    strategy = sgqlc.types.Field(ScriptLoadingStrategyEnum, graphql_name='strategy')


class EnqueuedStylesheet(sgqlc.types.Type, Node, EnqueuedAsset):
    __schema__ = schema
    __field_names__ = ('is_rtl', 'media', 'path', 'rel', 'suffix', 'title')
    is_rtl = sgqlc.types.Field(Boolean, graphql_name='isRtl')
    media = sgqlc.types.Field(String, graphql_name='media')
    path = sgqlc.types.Field(String, graphql_name='path')
    rel = sgqlc.types.Field(String, graphql_name='rel')
    suffix = sgqlc.types.Field(String, graphql_name='suffix')
    title = sgqlc.types.Field(String, graphql_name='title')


class Event(sgqlc.types.Type, Node, ContentNode, UniformResourceIdentifiable, DatabaseIdentifier, NodeWithTemplate, Previewable, NodeWithTitle, NodeWithContentEditor, NodeWithAuthor, NodeWithFeaturedImage, NodeWithExcerpt, NodeWithComments, NodeWithRevisions, MenuItemLinkable):
    __schema__ = schema
    __field_names__ = ('all_day', 'comments', 'cost', 'cost_max', 'cost_min', 'currency_position', 'currency_symbol', 'duration', 'end_date', 'events_categories', 'featured', 'has_password', 'hide_from_upcoming', 'linked_data', 'organizers', 'origin', 'password', 'phone', 'preview', 'revisions', 'show_map', 'show_map_link', 'start_date', 'tags', 'terms', 'timezone', 'timezone_abbr', 'url', 'venue')
    all_day = sgqlc.types.Field(Boolean, graphql_name='allDay')
    comments = sgqlc.types.Field('EventToCommentConnection', graphql_name='comments', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(EventToCommentConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    cost = sgqlc.types.Field(String, graphql_name='cost')
    cost_max = sgqlc.types.Field(String, graphql_name='costMax')
    cost_min = sgqlc.types.Field(String, graphql_name='costMin')
    currency_position = sgqlc.types.Field(String, graphql_name='currencyPosition')
    currency_symbol = sgqlc.types.Field(String, graphql_name='currencySymbol')
    duration = sgqlc.types.Field(Float, graphql_name='duration')
    end_date = sgqlc.types.Field(String, graphql_name='endDate')
    events_categories = sgqlc.types.Field('EventToEventsCategoryConnection', graphql_name='eventsCategories', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(EventToEventsCategoryConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    featured = sgqlc.types.Field(Boolean, graphql_name='featured')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    hide_from_upcoming = sgqlc.types.Field(Boolean, graphql_name='hideFromUpcoming')
    linked_data = sgqlc.types.Field(EventLinkedData, graphql_name='linkedData')
    organizers = sgqlc.types.Field('EventToOrganizerConnection', graphql_name='organizers', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(EventToOrganizerConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    origin = sgqlc.types.Field(String, graphql_name='origin')
    password = sgqlc.types.Field(String, graphql_name='password')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    preview = sgqlc.types.Field('EventToPreviewConnectionEdge', graphql_name='preview')
    revisions = sgqlc.types.Field('EventToRevisionConnection', graphql_name='revisions', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(EventToRevisionConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    show_map = sgqlc.types.Field(Boolean, graphql_name='showMap')
    show_map_link = sgqlc.types.Field(Boolean, graphql_name='showMapLink')
    start_date = sgqlc.types.Field(String, graphql_name='startDate')
    tags = sgqlc.types.Field('EventToTagConnection', graphql_name='tags', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(EventToTagConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    terms = sgqlc.types.Field('EventToTermNodeConnection', graphql_name='terms', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(EventToTermNodeConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    timezone = sgqlc.types.Field(String, graphql_name='timezone')
    timezone_abbr = sgqlc.types.Field(String, graphql_name='timezoneAbbr')
    url = sgqlc.types.Field(String, graphql_name='url')
    venue = sgqlc.types.Field('Venue', graphql_name='venue')


class EventToCommentConnection(sgqlc.types.relay.Connection, CommentConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class EventToCommentConnectionEdge(sgqlc.types.Type, CommentConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class EventToCommentConnectionPageInfo(sgqlc.types.Type, CommentConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class EventToEventConnection(sgqlc.types.relay.Connection, EventConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class EventToEventConnectionEdge(sgqlc.types.Type, EventConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class EventToEventConnectionPageInfo(sgqlc.types.Type, EventConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class EventToEventsCategoryConnection(sgqlc.types.relay.Connection, EventsCategoryConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class EventToEventsCategoryConnectionEdge(sgqlc.types.Type, EventsCategoryConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class EventToEventsCategoryConnectionPageInfo(sgqlc.types.Type, EventsCategoryConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class EventToOrganizerConnection(sgqlc.types.relay.Connection, OrganizerConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class EventToOrganizerConnectionEdge(sgqlc.types.Type, OrganizerConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class EventToOrganizerConnectionPageInfo(sgqlc.types.Type, OrganizerConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class EventToParentConnectionEdge(sgqlc.types.Type, OneToOneConnection, Edge, EventConnectionEdge):
    __schema__ = schema
    __field_names__ = ()


class EventToPreviewConnectionEdge(sgqlc.types.Type, OneToOneConnection, Edge, EventConnectionEdge):
    __schema__ = schema
    __field_names__ = ()


class EventToRevisionConnection(sgqlc.types.relay.Connection, EventConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class EventToRevisionConnectionEdge(sgqlc.types.Type, EventConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class EventToRevisionConnectionPageInfo(sgqlc.types.Type, EventConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class EventToTagConnection(sgqlc.types.relay.Connection, TagConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class EventToTagConnectionEdge(sgqlc.types.Type, TagConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class EventToTagConnectionPageInfo(sgqlc.types.Type, TagConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class EventToTermNodeConnection(sgqlc.types.relay.Connection, TermNodeConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class EventToTermNodeConnectionEdge(sgqlc.types.Type, TermNodeConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class EventToTermNodeConnectionPageInfo(sgqlc.types.Type, TermNodeConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class EventsCategory(sgqlc.types.Type, Node, TermNode, UniformResourceIdentifiable, DatabaseIdentifier, HierarchicalTermNode, HierarchicalNode, MenuItemLinkable):
    __schema__ = schema
    __field_names__ = ('ancestors', 'children', 'content_nodes', 'events', 'parent', 'taxonomy')
    ancestors = sgqlc.types.Field('EventsCategoryToAncestorsEventsCategoryConnection', graphql_name='ancestors', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    children = sgqlc.types.Field('EventsCategoryToEventsCategoryConnection', graphql_name='children', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(EventsCategoryToEventsCategoryConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    content_nodes = sgqlc.types.Field('EventsCategoryToContentNodeConnection', graphql_name='contentNodes', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(EventsCategoryToContentNodeConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    events = sgqlc.types.Field('EventsCategoryToEventConnection', graphql_name='events', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(EventsCategoryToEventConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    parent = sgqlc.types.Field('EventsCategoryToParentEventsCategoryConnectionEdge', graphql_name='parent')
    taxonomy = sgqlc.types.Field('EventsCategoryToTaxonomyConnectionEdge', graphql_name='taxonomy')


class EventsCategoryToAncestorsEventsCategoryConnection(sgqlc.types.relay.Connection, EventsCategoryConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class EventsCategoryToAncestorsEventsCategoryConnectionEdge(sgqlc.types.Type, EventsCategoryConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class EventsCategoryToAncestorsEventsCategoryConnectionPageInfo(sgqlc.types.Type, EventsCategoryConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class EventsCategoryToContentNodeConnection(sgqlc.types.relay.Connection, ContentNodeConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class EventsCategoryToContentNodeConnectionEdge(sgqlc.types.Type, ContentNodeConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class EventsCategoryToContentNodeConnectionPageInfo(sgqlc.types.Type, ContentNodeConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class EventsCategoryToEventConnection(sgqlc.types.relay.Connection, EventConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class EventsCategoryToEventConnectionEdge(sgqlc.types.Type, EventConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class EventsCategoryToEventConnectionPageInfo(sgqlc.types.Type, EventConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class EventsCategoryToEventsCategoryConnection(sgqlc.types.relay.Connection, EventsCategoryConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class EventsCategoryToEventsCategoryConnectionEdge(sgqlc.types.Type, EventsCategoryConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class EventsCategoryToEventsCategoryConnectionPageInfo(sgqlc.types.Type, EventsCategoryConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class EventsCategoryToParentEventsCategoryConnectionEdge(sgqlc.types.Type, OneToOneConnection, Edge, EventsCategoryConnectionEdge):
    __schema__ = schema
    __field_names__ = ()


class EventsCategoryToTaxonomyConnectionEdge(sgqlc.types.Type, OneToOneConnection, Edge, TaxonomyConnectionEdge):
    __schema__ = schema
    __field_names__ = ()


class GraphqlDocument(sgqlc.types.Type, Node, ContentNode, UniformResourceIdentifiable, DatabaseIdentifier, NodeWithTemplate, NodeWithTitle, NodeWithContentEditor):
    __schema__ = schema
    __field_names__ = ('alias', 'description', 'grant', 'graphql_document_groups', 'has_password', 'max_age_header', 'password', 'terms')
    alias = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='alias')
    description = sgqlc.types.Field(String, graphql_name='description')
    grant = sgqlc.types.Field(String, graphql_name='grant')
    graphql_document_groups = sgqlc.types.Field('GraphqlDocumentToGraphqlDocumentGroupConnection', graphql_name='graphqlDocumentGroups', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(GraphqlDocumentToGraphqlDocumentGroupConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    max_age_header = sgqlc.types.Field(Int, graphql_name='maxAgeHeader')
    password = sgqlc.types.Field(String, graphql_name='password')
    terms = sgqlc.types.Field('GraphqlDocumentToTermNodeConnection', graphql_name='terms', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(GraphqlDocumentToTermNodeConnectionWhereArgs, graphql_name='where', default=None)),
))
    )


class GraphqlDocumentGroup(sgqlc.types.Type, Node, TermNode, UniformResourceIdentifiable, DatabaseIdentifier):
    __schema__ = schema
    __field_names__ = ('content_nodes', 'graphql_documents', 'taxonomy')
    content_nodes = sgqlc.types.Field('GraphqlDocumentGroupToContentNodeConnection', graphql_name='contentNodes', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(GraphqlDocumentGroupToContentNodeConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    graphql_documents = sgqlc.types.Field('GraphqlDocumentGroupToGraphqlDocumentConnection', graphql_name='graphqlDocuments', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(GraphqlDocumentGroupToGraphqlDocumentConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    taxonomy = sgqlc.types.Field('GraphqlDocumentGroupToTaxonomyConnectionEdge', graphql_name='taxonomy')


class GraphqlDocumentGroupToContentNodeConnection(sgqlc.types.relay.Connection, ContentNodeConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class GraphqlDocumentGroupToContentNodeConnectionEdge(sgqlc.types.Type, ContentNodeConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class GraphqlDocumentGroupToContentNodeConnectionPageInfo(sgqlc.types.Type, ContentNodeConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class GraphqlDocumentGroupToGraphqlDocumentConnection(sgqlc.types.relay.Connection, GraphqlDocumentConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class GraphqlDocumentGroupToGraphqlDocumentConnectionEdge(sgqlc.types.Type, GraphqlDocumentConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class GraphqlDocumentGroupToGraphqlDocumentConnectionPageInfo(sgqlc.types.Type, GraphqlDocumentConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class GraphqlDocumentGroupToTaxonomyConnectionEdge(sgqlc.types.Type, OneToOneConnection, Edge, TaxonomyConnectionEdge):
    __schema__ = schema
    __field_names__ = ()


class GraphqlDocumentToGraphqlDocumentConnection(sgqlc.types.relay.Connection, GraphqlDocumentConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class GraphqlDocumentToGraphqlDocumentConnectionEdge(sgqlc.types.Type, GraphqlDocumentConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class GraphqlDocumentToGraphqlDocumentConnectionPageInfo(sgqlc.types.Type, GraphqlDocumentConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class GraphqlDocumentToGraphqlDocumentGroupConnection(sgqlc.types.relay.Connection, GraphqlDocumentGroupConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class GraphqlDocumentToGraphqlDocumentGroupConnectionEdge(sgqlc.types.Type, GraphqlDocumentGroupConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class GraphqlDocumentToGraphqlDocumentGroupConnectionPageInfo(sgqlc.types.Type, GraphqlDocumentGroupConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class GraphqlDocumentToParentConnectionEdge(sgqlc.types.Type, OneToOneConnection, Edge, GraphqlDocumentConnectionEdge):
    __schema__ = schema
    __field_names__ = ()


class GraphqlDocumentToPreviewConnectionEdge(sgqlc.types.Type, OneToOneConnection, Edge, GraphqlDocumentConnectionEdge):
    __schema__ = schema
    __field_names__ = ()


class GraphqlDocumentToTermNodeConnection(sgqlc.types.relay.Connection, TermNodeConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class GraphqlDocumentToTermNodeConnectionEdge(sgqlc.types.Type, TermNodeConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class GraphqlDocumentToTermNodeConnectionPageInfo(sgqlc.types.Type, TermNodeConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class HierarchicalContentNodeToContentNodeAncestorsConnection(sgqlc.types.relay.Connection, ContentNodeConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class HierarchicalContentNodeToContentNodeAncestorsConnectionEdge(sgqlc.types.Type, ContentNodeConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class HierarchicalContentNodeToContentNodeAncestorsConnectionPageInfo(sgqlc.types.Type, ContentNodeConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class HierarchicalContentNodeToContentNodeChildrenConnection(sgqlc.types.relay.Connection, ContentNodeConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class HierarchicalContentNodeToContentNodeChildrenConnectionEdge(sgqlc.types.Type, ContentNodeConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class HierarchicalContentNodeToContentNodeChildrenConnectionPageInfo(sgqlc.types.Type, ContentNodeConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class HierarchicalContentNodeToParentContentNodeConnectionEdge(sgqlc.types.Type, OneToOneConnection, Edge, ContentNodeConnectionEdge):
    __schema__ = schema
    __field_names__ = ()


class Job(sgqlc.types.Type, Node, ContentNode, UniformResourceIdentifiable, DatabaseIdentifier, NodeWithTemplate, Previewable, NodeWithTitle, NodeWithAuthor, MenuItemLinkable, WithAcfJobAcf):
    __schema__ = schema
    __field_names__ = ('contractkinds', 'has_password', 'jobmodes', 'occupationkinds', 'password', 'preview', 'terms')
    contractkinds = sgqlc.types.Field('JobToContractKindConnection', graphql_name='contractkinds', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(JobToContractKindConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    jobmodes = sgqlc.types.Field('JobToJobmodeConnection', graphql_name='jobmodes', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(JobToJobmodeConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    occupationkinds = sgqlc.types.Field('JobToOccupationkindConnection', graphql_name='occupationkinds', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(JobToOccupationkindConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    password = sgqlc.types.Field(String, graphql_name='password')
    preview = sgqlc.types.Field('JobToPreviewConnectionEdge', graphql_name='preview')
    terms = sgqlc.types.Field('JobToTermNodeConnection', graphql_name='terms', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(JobToTermNodeConnectionWhereArgs, graphql_name='where', default=None)),
))
    )


class JobAcf(sgqlc.types.Type, JobAcf_Fields, AcfFieldGroup, AcfFieldGroupFields):
    __schema__ = schema
    __field_names__ = ()


class JobToContractKindConnection(sgqlc.types.relay.Connection, ContractKindConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class JobToContractKindConnectionEdge(sgqlc.types.Type, ContractKindConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class JobToContractKindConnectionPageInfo(sgqlc.types.Type, ContractKindConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class JobToJobConnection(sgqlc.types.relay.Connection, JobConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class JobToJobConnectionEdge(sgqlc.types.Type, JobConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class JobToJobConnectionPageInfo(sgqlc.types.Type, JobConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class JobToJobmodeConnection(sgqlc.types.relay.Connection, JobmodeConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class JobToJobmodeConnectionEdge(sgqlc.types.Type, JobmodeConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class JobToJobmodeConnectionPageInfo(sgqlc.types.Type, JobmodeConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class JobToOccupationkindConnection(sgqlc.types.relay.Connection, OccupationkindConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class JobToOccupationkindConnectionEdge(sgqlc.types.Type, OccupationkindConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class JobToOccupationkindConnectionPageInfo(sgqlc.types.Type, OccupationkindConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class JobToParentConnectionEdge(sgqlc.types.Type, OneToOneConnection, Edge, JobConnectionEdge):
    __schema__ = schema
    __field_names__ = ()


class JobToPreviewConnectionEdge(sgqlc.types.Type, OneToOneConnection, Edge, JobConnectionEdge):
    __schema__ = schema
    __field_names__ = ()


class JobToTermNodeConnection(sgqlc.types.relay.Connection, TermNodeConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class JobToTermNodeConnectionEdge(sgqlc.types.Type, TermNodeConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class JobToTermNodeConnectionPageInfo(sgqlc.types.Type, TermNodeConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class Jobmode(sgqlc.types.Type, Node, TermNode, UniformResourceIdentifiable, DatabaseIdentifier, MenuItemLinkable):
    __schema__ = schema
    __field_names__ = ('content_nodes', 'jobs', 'taxonomy')
    content_nodes = sgqlc.types.Field('JobmodeToContentNodeConnection', graphql_name='contentNodes', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(JobmodeToContentNodeConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    jobs = sgqlc.types.Field('JobmodeToJobConnection', graphql_name='jobs', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(JobmodeToJobConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    taxonomy = sgqlc.types.Field('JobmodeToTaxonomyConnectionEdge', graphql_name='taxonomy')


class JobmodeToContentNodeConnection(sgqlc.types.relay.Connection, ContentNodeConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class JobmodeToContentNodeConnectionEdge(sgqlc.types.Type, ContentNodeConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class JobmodeToContentNodeConnectionPageInfo(sgqlc.types.Type, ContentNodeConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class JobmodeToJobConnection(sgqlc.types.relay.Connection, JobConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class JobmodeToJobConnectionEdge(sgqlc.types.Type, JobConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class JobmodeToJobConnectionPageInfo(sgqlc.types.Type, JobConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class JobmodeToTaxonomyConnectionEdge(sgqlc.types.Type, OneToOneConnection, Edge, TaxonomyConnectionEdge):
    __schema__ = schema
    __field_names__ = ()


class MediaItem(sgqlc.types.Type, Node, ContentNode, UniformResourceIdentifiable, DatabaseIdentifier, NodeWithTemplate, NodeWithTitle, NodeWithAuthor, NodeWithComments, HierarchicalContentNode, HierarchicalNode):
    __schema__ = schema
    __field_names__ = ('alt_text', 'caption', 'comments', 'description', 'file_size', 'has_password', 'media_details', 'media_item_url', 'media_type', 'mime_type', 'password', 'sizes', 'source_url', 'src_set')
    alt_text = sgqlc.types.Field(String, graphql_name='altText')
    caption = sgqlc.types.Field(String, graphql_name='caption', args=sgqlc.types.ArgDict((
        ('format', sgqlc.types.Arg(PostObjectFieldFormatEnum, graphql_name='format', default=None)),
))
    )
    comments = sgqlc.types.Field('MediaItemToCommentConnection', graphql_name='comments', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(MediaItemToCommentConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    description = sgqlc.types.Field(String, graphql_name='description', args=sgqlc.types.ArgDict((
        ('format', sgqlc.types.Arg(PostObjectFieldFormatEnum, graphql_name='format', default=None)),
))
    )
    file_size = sgqlc.types.Field(Int, graphql_name='fileSize', args=sgqlc.types.ArgDict((
        ('size', sgqlc.types.Arg(MediaItemSizeEnum, graphql_name='size', default=None)),
))
    )
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    media_details = sgqlc.types.Field(MediaDetails, graphql_name='mediaDetails')
    media_item_url = sgqlc.types.Field(String, graphql_name='mediaItemUrl')
    media_type = sgqlc.types.Field(String, graphql_name='mediaType')
    mime_type = sgqlc.types.Field(String, graphql_name='mimeType')
    password = sgqlc.types.Field(String, graphql_name='password')
    sizes = sgqlc.types.Field(String, graphql_name='sizes', args=sgqlc.types.ArgDict((
        ('size', sgqlc.types.Arg(MediaItemSizeEnum, graphql_name='size', default=None)),
))
    )
    source_url = sgqlc.types.Field(String, graphql_name='sourceUrl', args=sgqlc.types.ArgDict((
        ('size', sgqlc.types.Arg(MediaItemSizeEnum, graphql_name='size', default=None)),
))
    )
    src_set = sgqlc.types.Field(String, graphql_name='srcSet', args=sgqlc.types.ArgDict((
        ('size', sgqlc.types.Arg(MediaItemSizeEnum, graphql_name='size', default=None)),
))
    )


class MediaItemToCommentConnection(sgqlc.types.relay.Connection, CommentConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class MediaItemToCommentConnectionEdge(sgqlc.types.Type, CommentConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class MediaItemToCommentConnectionPageInfo(sgqlc.types.Type, CommentConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class Menu(sgqlc.types.Type, Node, DatabaseIdentifier):
    __schema__ = schema
    __field_names__ = ('count', 'is_restricted', 'locations', 'menu_items', 'name', 'slug')
    count = sgqlc.types.Field(Int, graphql_name='count')
    is_restricted = sgqlc.types.Field(Boolean, graphql_name='isRestricted')
    locations = sgqlc.types.Field(sgqlc.types.list_of(MenuLocationEnum), graphql_name='locations')
    menu_items = sgqlc.types.Field('MenuToMenuItemConnection', graphql_name='menuItems', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(MenuToMenuItemConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    name = sgqlc.types.Field(String, graphql_name='name')
    slug = sgqlc.types.Field(String, graphql_name='slug')


class MenuItem(sgqlc.types.Type, Node, DatabaseIdentifier):
    __schema__ = schema
    __field_names__ = ('child_items', 'connected_node', 'css_classes', 'description', 'is_restricted', 'label', 'link_relationship', 'locations', 'menu', 'order', 'parent_database_id', 'parent_id', 'path', 'target', 'title', 'uri', 'url')
    child_items = sgqlc.types.Field('MenuItemToMenuItemConnection', graphql_name='childItems', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(MenuItemToMenuItemConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    connected_node = sgqlc.types.Field('MenuItemToMenuItemLinkableConnectionEdge', graphql_name='connectedNode')
    css_classes = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='cssClasses')
    description = sgqlc.types.Field(String, graphql_name='description')
    is_restricted = sgqlc.types.Field(Boolean, graphql_name='isRestricted')
    label = sgqlc.types.Field(String, graphql_name='label')
    link_relationship = sgqlc.types.Field(String, graphql_name='linkRelationship')
    locations = sgqlc.types.Field(sgqlc.types.list_of(MenuLocationEnum), graphql_name='locations')
    menu = sgqlc.types.Field('MenuItemToMenuConnectionEdge', graphql_name='menu')
    order = sgqlc.types.Field(Int, graphql_name='order')
    parent_database_id = sgqlc.types.Field(Int, graphql_name='parentDatabaseId')
    parent_id = sgqlc.types.Field(ID, graphql_name='parentId')
    path = sgqlc.types.Field(String, graphql_name='path')
    target = sgqlc.types.Field(String, graphql_name='target')
    title = sgqlc.types.Field(String, graphql_name='title')
    uri = sgqlc.types.Field(String, graphql_name='uri')
    url = sgqlc.types.Field(String, graphql_name='url')


class MenuItemToMenuConnectionEdge(sgqlc.types.Type, OneToOneConnection, Edge, MenuConnectionEdge):
    __schema__ = schema
    __field_names__ = ()


class MenuItemToMenuItemConnection(sgqlc.types.relay.Connection, MenuItemConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class MenuItemToMenuItemConnectionEdge(sgqlc.types.Type, MenuItemConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class MenuItemToMenuItemConnectionPageInfo(sgqlc.types.Type, MenuItemConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class MenuItemToMenuItemLinkableConnectionEdge(sgqlc.types.Type, OneToOneConnection, Edge, MenuItemLinkableConnectionEdge):
    __schema__ = schema
    __field_names__ = ()


class MenuToMenuItemConnection(sgqlc.types.relay.Connection, MenuItemConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class MenuToMenuItemConnectionEdge(sgqlc.types.Type, MenuItemConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class MenuToMenuItemConnectionPageInfo(sgqlc.types.Type, MenuItemConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class NodeWithAuthorToUserConnectionEdge(sgqlc.types.Type, OneToOneConnection, Edge, UserConnectionEdge):
    __schema__ = schema
    __field_names__ = ()


class NodeWithFeaturedImageToMediaItemConnectionEdge(sgqlc.types.Type, OneToOneConnection, Edge, MediaItemConnectionEdge):
    __schema__ = schema
    __field_names__ = ()


class NodeWithRevisionsToContentNodeConnectionEdge(sgqlc.types.Type, OneToOneConnection, Edge, ContentNodeConnectionEdge):
    __schema__ = schema
    __field_names__ = ()


class Occupationkind(sgqlc.types.Type, Node, TermNode, UniformResourceIdentifiable, DatabaseIdentifier, MenuItemLinkable):
    __schema__ = schema
    __field_names__ = ('content_nodes', 'jobs', 'taxonomy')
    content_nodes = sgqlc.types.Field('OccupationkindToContentNodeConnection', graphql_name='contentNodes', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(OccupationkindToContentNodeConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    jobs = sgqlc.types.Field('OccupationkindToJobConnection', graphql_name='jobs', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(OccupationkindToJobConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    taxonomy = sgqlc.types.Field('OccupationkindToTaxonomyConnectionEdge', graphql_name='taxonomy')


class OccupationkindToContentNodeConnection(sgqlc.types.relay.Connection, ContentNodeConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class OccupationkindToContentNodeConnectionEdge(sgqlc.types.Type, ContentNodeConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class OccupationkindToContentNodeConnectionPageInfo(sgqlc.types.Type, ContentNodeConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class OccupationkindToJobConnection(sgqlc.types.relay.Connection, JobConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class OccupationkindToJobConnectionEdge(sgqlc.types.Type, JobConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class OccupationkindToJobConnectionPageInfo(sgqlc.types.Type, JobConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class OccupationkindToTaxonomyConnectionEdge(sgqlc.types.Type, OneToOneConnection, Edge, TaxonomyConnectionEdge):
    __schema__ = schema
    __field_names__ = ()


class Organizer(sgqlc.types.Type, Node, ContentNode, UniformResourceIdentifiable, DatabaseIdentifier, NodeWithTemplate, NodeWithTitle, NodeWithContentEditor, NodeWithAuthor, NodeWithFeaturedImage, NodeWithExcerpt, NodeWithRevisions):
    __schema__ = schema
    __field_names__ = ('email', 'has_password', 'linked_data', 'password', 'phone', 'revisions', 'website')
    email = sgqlc.types.Field(String, graphql_name='email')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    linked_data = sgqlc.types.Field(OrganizerLinkedData, graphql_name='linkedData')
    password = sgqlc.types.Field(String, graphql_name='password')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    revisions = sgqlc.types.Field('OrganizerToRevisionConnection', graphql_name='revisions', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(OrganizerToRevisionConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    website = sgqlc.types.Field(String, graphql_name='website')


class OrganizerToOrganizerConnection(sgqlc.types.relay.Connection, OrganizerConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class OrganizerToOrganizerConnectionEdge(sgqlc.types.Type, OrganizerConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class OrganizerToOrganizerConnectionPageInfo(sgqlc.types.Type, OrganizerConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class OrganizerToParentConnectionEdge(sgqlc.types.Type, OneToOneConnection, Edge, OrganizerConnectionEdge):
    __schema__ = schema
    __field_names__ = ()


class OrganizerToPreviewConnectionEdge(sgqlc.types.Type, OneToOneConnection, Edge, OrganizerConnectionEdge):
    __schema__ = schema
    __field_names__ = ()


class OrganizerToRevisionConnection(sgqlc.types.relay.Connection, OrganizerConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class OrganizerToRevisionConnectionEdge(sgqlc.types.Type, OrganizerConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class OrganizerToRevisionConnectionPageInfo(sgqlc.types.Type, OrganizerConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class Page(sgqlc.types.Type, Node, ContentNode, UniformResourceIdentifiable, DatabaseIdentifier, NodeWithTemplate, Previewable, NodeWithTitle, NodeWithContentEditor, NodeWithAuthor, NodeWithFeaturedImage, NodeWithComments, NodeWithRevisions, NodeWithPageAttributes, HierarchicalContentNode, HierarchicalNode, MenuItemLinkable):
    __schema__ = schema
    __field_names__ = ('comments', 'has_password', 'is_privacy_page', 'password', 'preview', 'revisions')
    comments = sgqlc.types.Field('PageToCommentConnection', graphql_name='comments', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(PageToCommentConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    is_privacy_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPrivacyPage')
    password = sgqlc.types.Field(String, graphql_name='password')
    preview = sgqlc.types.Field('PageToPreviewConnectionEdge', graphql_name='preview')
    revisions = sgqlc.types.Field('PageToRevisionConnection', graphql_name='revisions', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(PageToRevisionConnectionWhereArgs, graphql_name='where', default=None)),
))
    )


class PageToCommentConnection(sgqlc.types.relay.Connection, CommentConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class PageToCommentConnectionEdge(sgqlc.types.Type, CommentConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class PageToCommentConnectionPageInfo(sgqlc.types.Type, CommentConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class PageToPreviewConnectionEdge(sgqlc.types.Type, OneToOneConnection, Edge, PageConnectionEdge):
    __schema__ = schema
    __field_names__ = ()


class PageToRevisionConnection(sgqlc.types.relay.Connection, PageConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class PageToRevisionConnectionEdge(sgqlc.types.Type, PageConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class PageToRevisionConnectionPageInfo(sgqlc.types.Type, PageConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class Partner(sgqlc.types.Type, Node, ContentNode, UniformResourceIdentifiable, DatabaseIdentifier, NodeWithTemplate, Previewable, NodeWithTitle, NodeWithAuthor, MenuItemLinkable, WithAcfPartnerAcf):
    __schema__ = schema
    __field_names__ = ('has_password', 'password', 'preview')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    password = sgqlc.types.Field(String, graphql_name='password')
    preview = sgqlc.types.Field('PartnerToPreviewConnectionEdge', graphql_name='preview')


class PartnerAcf(sgqlc.types.Type, PartnerAcf_Fields, AcfFieldGroup, AcfFieldGroupFields):
    __schema__ = schema
    __field_names__ = ()


class PartnerToParentConnectionEdge(sgqlc.types.Type, OneToOneConnection, Edge, PartnerConnectionEdge):
    __schema__ = schema
    __field_names__ = ()


class PartnerToPartnerConnection(sgqlc.types.relay.Connection, PartnerConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class PartnerToPartnerConnectionEdge(sgqlc.types.Type, PartnerConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class PartnerToPartnerConnectionPageInfo(sgqlc.types.Type, PartnerConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class PartnerToPreviewConnectionEdge(sgqlc.types.Type, OneToOneConnection, Edge, PartnerConnectionEdge):
    __schema__ = schema
    __field_names__ = ()


class Plugin(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('author', 'author_uri', 'description', 'is_restricted', 'name', 'path', 'plugin_uri', 'version')
    author = sgqlc.types.Field(String, graphql_name='author')
    author_uri = sgqlc.types.Field(String, graphql_name='authorUri')
    description = sgqlc.types.Field(String, graphql_name='description')
    is_restricted = sgqlc.types.Field(Boolean, graphql_name='isRestricted')
    name = sgqlc.types.Field(String, graphql_name='name')
    path = sgqlc.types.Field(String, graphql_name='path')
    plugin_uri = sgqlc.types.Field(String, graphql_name='pluginUri')
    version = sgqlc.types.Field(String, graphql_name='version')


class Post(sgqlc.types.Type, Node, ContentNode, UniformResourceIdentifiable, DatabaseIdentifier, NodeWithTemplate, Previewable, NodeWithTitle, NodeWithContentEditor, NodeWithAuthor, NodeWithFeaturedImage, NodeWithExcerpt, NodeWithComments, NodeWithTrackbacks, NodeWithRevisions, MenuItemLinkable):
    __schema__ = schema
    __field_names__ = ('categories', 'comments', 'has_password', 'is_sticky', 'password', 'post_formats', 'preview', 'revisions', 'tags', 'terms')
    categories = sgqlc.types.Field('PostToCategoryConnection', graphql_name='categories', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(PostToCategoryConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    comments = sgqlc.types.Field('PostToCommentConnection', graphql_name='comments', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(PostToCommentConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    is_sticky = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSticky')
    password = sgqlc.types.Field(String, graphql_name='password')
    post_formats = sgqlc.types.Field('PostToPostFormatConnection', graphql_name='postFormats', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(PostToPostFormatConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    preview = sgqlc.types.Field('PostToPreviewConnectionEdge', graphql_name='preview')
    revisions = sgqlc.types.Field('PostToRevisionConnection', graphql_name='revisions', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(PostToRevisionConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    tags = sgqlc.types.Field('PostToTagConnection', graphql_name='tags', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(PostToTagConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    terms = sgqlc.types.Field('PostToTermNodeConnection', graphql_name='terms', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(PostToTermNodeConnectionWhereArgs, graphql_name='where', default=None)),
))
    )


class PostFormat(sgqlc.types.Type, Node, TermNode, UniformResourceIdentifiable, DatabaseIdentifier):
    __schema__ = schema
    __field_names__ = ('content_nodes', 'posts', 'taxonomy')
    content_nodes = sgqlc.types.Field('PostFormatToContentNodeConnection', graphql_name='contentNodes', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(PostFormatToContentNodeConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    posts = sgqlc.types.Field('PostFormatToPostConnection', graphql_name='posts', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(PostFormatToPostConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    taxonomy = sgqlc.types.Field('PostFormatToTaxonomyConnectionEdge', graphql_name='taxonomy')


class PostFormatToContentNodeConnection(sgqlc.types.relay.Connection, ContentNodeConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class PostFormatToContentNodeConnectionEdge(sgqlc.types.Type, ContentNodeConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class PostFormatToContentNodeConnectionPageInfo(sgqlc.types.Type, ContentNodeConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class PostFormatToPostConnection(sgqlc.types.relay.Connection, PostConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class PostFormatToPostConnectionEdge(sgqlc.types.Type, PostConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class PostFormatToPostConnectionPageInfo(sgqlc.types.Type, PostConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class PostFormatToTaxonomyConnectionEdge(sgqlc.types.Type, OneToOneConnection, Edge, TaxonomyConnectionEdge):
    __schema__ = schema
    __field_names__ = ()


class PostToCategoryConnection(sgqlc.types.relay.Connection, CategoryConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class PostToCategoryConnectionEdge(sgqlc.types.Type, CategoryConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class PostToCategoryConnectionPageInfo(sgqlc.types.Type, CategoryConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class PostToCommentConnection(sgqlc.types.relay.Connection, CommentConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class PostToCommentConnectionEdge(sgqlc.types.Type, CommentConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class PostToCommentConnectionPageInfo(sgqlc.types.Type, CommentConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class PostToParentConnectionEdge(sgqlc.types.Type, OneToOneConnection, Edge, PostConnectionEdge):
    __schema__ = schema
    __field_names__ = ()


class PostToPostConnection(sgqlc.types.relay.Connection, PostConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class PostToPostConnectionEdge(sgqlc.types.Type, PostConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class PostToPostConnectionPageInfo(sgqlc.types.Type, PostConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class PostToPostFormatConnection(sgqlc.types.relay.Connection, PostFormatConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class PostToPostFormatConnectionEdge(sgqlc.types.Type, PostFormatConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class PostToPostFormatConnectionPageInfo(sgqlc.types.Type, PostFormatConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class PostToPreviewConnectionEdge(sgqlc.types.Type, OneToOneConnection, Edge, PostConnectionEdge):
    __schema__ = schema
    __field_names__ = ()


class PostToRevisionConnection(sgqlc.types.relay.Connection, PostConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class PostToRevisionConnectionEdge(sgqlc.types.Type, PostConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class PostToRevisionConnectionPageInfo(sgqlc.types.Type, PostConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class PostToTagConnection(sgqlc.types.relay.Connection, TagConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class PostToTagConnectionEdge(sgqlc.types.Type, TagConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class PostToTagConnectionPageInfo(sgqlc.types.Type, TagConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class PostToTermNodeConnection(sgqlc.types.relay.Connection, TermNodeConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class PostToTermNodeConnectionEdge(sgqlc.types.Type, TermNodeConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class PostToTermNodeConnectionPageInfo(sgqlc.types.Type, TermNodeConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToCategoryConnection(sgqlc.types.relay.Connection, CategoryConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToCategoryConnectionEdge(sgqlc.types.Type, CategoryConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToCategoryConnectionPageInfo(sgqlc.types.Type, CategoryConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToCommentConnection(sgqlc.types.relay.Connection, CommentConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToCommentConnectionEdge(sgqlc.types.Type, CommentConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToCommentConnectionPageInfo(sgqlc.types.Type, CommentConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToContentNodeConnection(sgqlc.types.relay.Connection, ContentNodeConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToContentNodeConnectionEdge(sgqlc.types.Type, ContentNodeConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToContentNodeConnectionPageInfo(sgqlc.types.Type, ContentNodeConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToContentTypeConnection(sgqlc.types.relay.Connection, ContentTypeConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToContentTypeConnectionEdge(sgqlc.types.Type, ContentTypeConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToContentTypeConnectionPageInfo(sgqlc.types.Type, ContentTypeConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToContractKindConnection(sgqlc.types.relay.Connection, ContractKindConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToContractKindConnectionEdge(sgqlc.types.Type, ContractKindConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToContractKindConnectionPageInfo(sgqlc.types.Type, ContractKindConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToEnqueuedScriptConnection(sgqlc.types.relay.Connection, EnqueuedScriptConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToEnqueuedScriptConnectionEdge(sgqlc.types.Type, EnqueuedScriptConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToEnqueuedScriptConnectionPageInfo(sgqlc.types.Type, EnqueuedScriptConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToEnqueuedStylesheetConnection(sgqlc.types.relay.Connection, EnqueuedStylesheetConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToEnqueuedStylesheetConnectionEdge(sgqlc.types.Type, EnqueuedStylesheetConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToEnqueuedStylesheetConnectionPageInfo(sgqlc.types.Type, EnqueuedStylesheetConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToEventConnection(sgqlc.types.relay.Connection, EventConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToEventConnectionEdge(sgqlc.types.Type, EventConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToEventConnectionPageInfo(sgqlc.types.Type, EventConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToEventsCategoryConnection(sgqlc.types.relay.Connection, EventsCategoryConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToEventsCategoryConnectionEdge(sgqlc.types.Type, EventsCategoryConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToEventsCategoryConnectionPageInfo(sgqlc.types.Type, EventsCategoryConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToGraphqlDocumentConnection(sgqlc.types.relay.Connection, GraphqlDocumentConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToGraphqlDocumentConnectionEdge(sgqlc.types.Type, GraphqlDocumentConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToGraphqlDocumentConnectionPageInfo(sgqlc.types.Type, GraphqlDocumentConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToGraphqlDocumentGroupConnection(sgqlc.types.relay.Connection, GraphqlDocumentGroupConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToGraphqlDocumentGroupConnectionEdge(sgqlc.types.Type, GraphqlDocumentGroupConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToGraphqlDocumentGroupConnectionPageInfo(sgqlc.types.Type, GraphqlDocumentGroupConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToJobConnection(sgqlc.types.relay.Connection, JobConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToJobConnectionEdge(sgqlc.types.Type, JobConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToJobConnectionPageInfo(sgqlc.types.Type, JobConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToJobmodeConnection(sgqlc.types.relay.Connection, JobmodeConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToJobmodeConnectionEdge(sgqlc.types.Type, JobmodeConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToJobmodeConnectionPageInfo(sgqlc.types.Type, JobmodeConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToMediaItemConnection(sgqlc.types.relay.Connection, MediaItemConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToMediaItemConnectionEdge(sgqlc.types.Type, MediaItemConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToMediaItemConnectionPageInfo(sgqlc.types.Type, MediaItemConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToMenuConnection(sgqlc.types.relay.Connection, MenuConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToMenuConnectionEdge(sgqlc.types.Type, MenuConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToMenuConnectionPageInfo(sgqlc.types.Type, MenuConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToMenuItemConnection(sgqlc.types.relay.Connection, MenuItemConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToMenuItemConnectionEdge(sgqlc.types.Type, MenuItemConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToMenuItemConnectionPageInfo(sgqlc.types.Type, MenuItemConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToOccupationkindConnection(sgqlc.types.relay.Connection, OccupationkindConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToOccupationkindConnectionEdge(sgqlc.types.Type, OccupationkindConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToOccupationkindConnectionPageInfo(sgqlc.types.Type, OccupationkindConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToOrganizerConnection(sgqlc.types.relay.Connection, OrganizerConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToOrganizerConnectionEdge(sgqlc.types.Type, OrganizerConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToOrganizerConnectionPageInfo(sgqlc.types.Type, OrganizerConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToPageConnection(sgqlc.types.relay.Connection, PageConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToPageConnectionEdge(sgqlc.types.Type, PageConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToPageConnectionPageInfo(sgqlc.types.Type, PageConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToPartnerConnection(sgqlc.types.relay.Connection, PartnerConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToPartnerConnectionEdge(sgqlc.types.Type, PartnerConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToPartnerConnectionPageInfo(sgqlc.types.Type, PartnerConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToPluginConnection(sgqlc.types.relay.Connection, PluginConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToPluginConnectionEdge(sgqlc.types.Type, PluginConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToPluginConnectionPageInfo(sgqlc.types.Type, PluginConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToPostConnection(sgqlc.types.relay.Connection, PostConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToPostConnectionEdge(sgqlc.types.Type, PostConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToPostConnectionPageInfo(sgqlc.types.Type, PostConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToPostFormatConnection(sgqlc.types.relay.Connection, PostFormatConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToPostFormatConnectionEdge(sgqlc.types.Type, PostFormatConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToPostFormatConnectionPageInfo(sgqlc.types.Type, PostFormatConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToRevisionsConnection(sgqlc.types.relay.Connection, ContentNodeConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToRevisionsConnectionEdge(sgqlc.types.Type, ContentNodeConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToRevisionsConnectionPageInfo(sgqlc.types.Type, ContentNodeConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToTagConnection(sgqlc.types.relay.Connection, TagConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToTagConnectionEdge(sgqlc.types.Type, TagConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToTagConnectionPageInfo(sgqlc.types.Type, TagConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToTaxonomyConnection(sgqlc.types.relay.Connection, TaxonomyConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToTaxonomyConnectionEdge(sgqlc.types.Type, TaxonomyConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToTaxonomyConnectionPageInfo(sgqlc.types.Type, TaxonomyConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToTermNodeConnection(sgqlc.types.relay.Connection, TermNodeConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToTermNodeConnectionEdge(sgqlc.types.Type, TermNodeConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToTermNodeConnectionPageInfo(sgqlc.types.Type, TermNodeConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToThemeConnection(sgqlc.types.relay.Connection, ThemeConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToThemeConnectionEdge(sgqlc.types.Type, ThemeConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToThemeConnectionPageInfo(sgqlc.types.Type, ThemeConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToUserConnection(sgqlc.types.relay.Connection, UserConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToUserConnectionEdge(sgqlc.types.Type, UserConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToUserConnectionPageInfo(sgqlc.types.Type, UserConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToUserRoleConnection(sgqlc.types.relay.Connection, UserRoleConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToUserRoleConnectionEdge(sgqlc.types.Type, UserRoleConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToUserRoleConnectionPageInfo(sgqlc.types.Type, UserRoleConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToVenueConnection(sgqlc.types.relay.Connection, VenueConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToVenueConnectionEdge(sgqlc.types.Type, VenueConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class RootQueryToVenueConnectionPageInfo(sgqlc.types.Type, VenueConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class Tag(sgqlc.types.Type, Node, TermNode, UniformResourceIdentifiable, DatabaseIdentifier, MenuItemLinkable):
    __schema__ = schema
    __field_names__ = ('content_nodes', 'events', 'posts', 'taxonomy')
    content_nodes = sgqlc.types.Field('TagToContentNodeConnection', graphql_name='contentNodes', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(TagToContentNodeConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    events = sgqlc.types.Field('TagToEventConnection', graphql_name='events', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(TagToEventConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    posts = sgqlc.types.Field('TagToPostConnection', graphql_name='posts', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(TagToPostConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    taxonomy = sgqlc.types.Field('TagToTaxonomyConnectionEdge', graphql_name='taxonomy')


class TagToContentNodeConnection(sgqlc.types.relay.Connection, ContentNodeConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class TagToContentNodeConnectionEdge(sgqlc.types.Type, ContentNodeConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class TagToContentNodeConnectionPageInfo(sgqlc.types.Type, ContentNodeConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class TagToEventConnection(sgqlc.types.relay.Connection, EventConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class TagToEventConnectionEdge(sgqlc.types.Type, EventConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class TagToEventConnectionPageInfo(sgqlc.types.Type, EventConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class TagToPostConnection(sgqlc.types.relay.Connection, PostConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class TagToPostConnectionEdge(sgqlc.types.Type, PostConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class TagToPostConnectionPageInfo(sgqlc.types.Type, PostConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class TagToTaxonomyConnectionEdge(sgqlc.types.Type, OneToOneConnection, Edge, TaxonomyConnectionEdge):
    __schema__ = schema
    __field_names__ = ()


class Taxonomy(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('connected_content_types', 'connected_terms', 'description', 'graphql_plural_name', 'graphql_single_name', 'hierarchical', 'is_restricted', 'label', 'name', 'public', 'rest_base', 'rest_controller_class', 'show_cloud', 'show_in_admin_column', 'show_in_graphql', 'show_in_menu', 'show_in_nav_menus', 'show_in_quick_edit', 'show_in_rest', 'show_ui')
    connected_content_types = sgqlc.types.Field('TaxonomyToContentTypeConnection', graphql_name='connectedContentTypes', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    connected_terms = sgqlc.types.Field('TaxonomyToTermNodeConnection', graphql_name='connectedTerms', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    description = sgqlc.types.Field(String, graphql_name='description')
    graphql_plural_name = sgqlc.types.Field(String, graphql_name='graphqlPluralName')
    graphql_single_name = sgqlc.types.Field(String, graphql_name='graphqlSingleName')
    hierarchical = sgqlc.types.Field(Boolean, graphql_name='hierarchical')
    is_restricted = sgqlc.types.Field(Boolean, graphql_name='isRestricted')
    label = sgqlc.types.Field(String, graphql_name='label')
    name = sgqlc.types.Field(String, graphql_name='name')
    public = sgqlc.types.Field(Boolean, graphql_name='public')
    rest_base = sgqlc.types.Field(String, graphql_name='restBase')
    rest_controller_class = sgqlc.types.Field(String, graphql_name='restControllerClass')
    show_cloud = sgqlc.types.Field(Boolean, graphql_name='showCloud')
    show_in_admin_column = sgqlc.types.Field(Boolean, graphql_name='showInAdminColumn')
    show_in_graphql = sgqlc.types.Field(Boolean, graphql_name='showInGraphql')
    show_in_menu = sgqlc.types.Field(Boolean, graphql_name='showInMenu')
    show_in_nav_menus = sgqlc.types.Field(Boolean, graphql_name='showInNavMenus')
    show_in_quick_edit = sgqlc.types.Field(Boolean, graphql_name='showInQuickEdit')
    show_in_rest = sgqlc.types.Field(Boolean, graphql_name='showInRest')
    show_ui = sgqlc.types.Field(Boolean, graphql_name='showUi')


class TaxonomyToContentTypeConnection(sgqlc.types.relay.Connection, ContentTypeConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class TaxonomyToContentTypeConnectionEdge(sgqlc.types.Type, ContentTypeConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class TaxonomyToContentTypeConnectionPageInfo(sgqlc.types.Type, ContentTypeConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class TaxonomyToTermNodeConnection(sgqlc.types.relay.Connection, TermNodeConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class TaxonomyToTermNodeConnectionEdge(sgqlc.types.Type, TermNodeConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class TaxonomyToTermNodeConnectionPageInfo(sgqlc.types.Type, TermNodeConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class Template_CalendarViewsEventArchive(sgqlc.types.Type, ContentTemplate):
    __schema__ = schema
    __field_names__ = ()


class Template_PageAvecColonneLatrale(sgqlc.types.Type, ContentTemplate):
    __schema__ = schema
    __field_names__ = ()


class Template_PageNoTitle(sgqlc.types.Type, ContentTemplate):
    __schema__ = schema
    __field_names__ = ()


class Template_PageWithWideImage(sgqlc.types.Type, ContentTemplate):
    __schema__ = schema
    __field_names__ = ()


class Template_SingleEvent(sgqlc.types.Type, ContentTemplate):
    __schema__ = schema
    __field_names__ = ()


class Template_SingleWithSidebar(sgqlc.types.Type, ContentTemplate):
    __schema__ = schema
    __field_names__ = ()


class TermNodeToEnqueuedScriptConnection(sgqlc.types.relay.Connection, EnqueuedScriptConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class TermNodeToEnqueuedScriptConnectionEdge(sgqlc.types.Type, EnqueuedScriptConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class TermNodeToEnqueuedScriptConnectionPageInfo(sgqlc.types.Type, EnqueuedScriptConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class TermNodeToEnqueuedStylesheetConnection(sgqlc.types.relay.Connection, EnqueuedStylesheetConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class TermNodeToEnqueuedStylesheetConnectionEdge(sgqlc.types.Type, EnqueuedStylesheetConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class TermNodeToEnqueuedStylesheetConnectionPageInfo(sgqlc.types.Type, EnqueuedStylesheetConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class Theme(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('author', 'author_uri', 'description', 'is_restricted', 'name', 'screenshot', 'slug', 'tags', 'theme_uri', 'version')
    author = sgqlc.types.Field(String, graphql_name='author')
    author_uri = sgqlc.types.Field(String, graphql_name='authorUri')
    description = sgqlc.types.Field(String, graphql_name='description')
    is_restricted = sgqlc.types.Field(Boolean, graphql_name='isRestricted')
    name = sgqlc.types.Field(String, graphql_name='name')
    screenshot = sgqlc.types.Field(String, graphql_name='screenshot')
    slug = sgqlc.types.Field(String, graphql_name='slug')
    tags = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tags')
    theme_uri = sgqlc.types.Field(String, graphql_name='themeUri')
    version = sgqlc.types.Field(String, graphql_name='version')


class User(sgqlc.types.Type, Node, UniformResourceIdentifiable, Commenter, DatabaseIdentifier):
    __schema__ = schema
    __field_names__ = ('cap_key', 'capabilities', 'comments', 'description', 'enqueued_scripts', 'enqueued_stylesheets', 'events', 'extra_capabilities', 'first_name', 'is_jwt_auth_secret_revoked', 'jobs', 'jwt_auth_expiration', 'jwt_auth_token', 'jwt_refresh_token', 'jwt_user_secret', 'last_name', 'locale', 'media_items', 'nicename', 'nickname', 'organizers', 'pages', 'partners', 'posts', 'registered_date', 'revisions', 'roles', 'should_show_admin_toolbar', 'slug', 'username', 'venues')
    cap_key = sgqlc.types.Field(String, graphql_name='capKey')
    capabilities = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='capabilities')
    comments = sgqlc.types.Field('UserToCommentConnection', graphql_name='comments', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(UserToCommentConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    description = sgqlc.types.Field(String, graphql_name='description')
    enqueued_scripts = sgqlc.types.Field('UserToEnqueuedScriptConnection', graphql_name='enqueuedScripts', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    enqueued_stylesheets = sgqlc.types.Field('UserToEnqueuedStylesheetConnection', graphql_name='enqueuedStylesheets', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    events = sgqlc.types.Field('UserToEventConnection', graphql_name='events', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(UserToEventConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    extra_capabilities = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='extraCapabilities')
    first_name = sgqlc.types.Field(String, graphql_name='firstName')
    is_jwt_auth_secret_revoked = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isJwtAuthSecretRevoked')
    jobs = sgqlc.types.Field('UserToJobConnection', graphql_name='jobs', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(UserToJobConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    jwt_auth_expiration = sgqlc.types.Field(String, graphql_name='jwtAuthExpiration')
    jwt_auth_token = sgqlc.types.Field(String, graphql_name='jwtAuthToken')
    jwt_refresh_token = sgqlc.types.Field(String, graphql_name='jwtRefreshToken')
    jwt_user_secret = sgqlc.types.Field(String, graphql_name='jwtUserSecret')
    last_name = sgqlc.types.Field(String, graphql_name='lastName')
    locale = sgqlc.types.Field(String, graphql_name='locale')
    media_items = sgqlc.types.Field('UserToMediaItemConnection', graphql_name='mediaItems', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(UserToMediaItemConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    nicename = sgqlc.types.Field(String, graphql_name='nicename')
    nickname = sgqlc.types.Field(String, graphql_name='nickname')
    organizers = sgqlc.types.Field('UserToOrganizerConnection', graphql_name='organizers', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(UserToOrganizerConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    pages = sgqlc.types.Field('UserToPageConnection', graphql_name='pages', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(UserToPageConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    partners = sgqlc.types.Field('UserToPartnerConnection', graphql_name='partners', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(UserToPartnerConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    posts = sgqlc.types.Field('UserToPostConnection', graphql_name='posts', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(UserToPostConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    registered_date = sgqlc.types.Field(String, graphql_name='registeredDate')
    revisions = sgqlc.types.Field('UserToRevisionsConnection', graphql_name='revisions', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(UserToRevisionsConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    roles = sgqlc.types.Field('UserToUserRoleConnection', graphql_name='roles', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
))
    )
    should_show_admin_toolbar = sgqlc.types.Field(Boolean, graphql_name='shouldShowAdminToolbar')
    slug = sgqlc.types.Field(String, graphql_name='slug')
    username = sgqlc.types.Field(String, graphql_name='username')
    venues = sgqlc.types.Field('UserToVenueConnection', graphql_name='venues', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(UserToVenueConnectionWhereArgs, graphql_name='where', default=None)),
))
    )


class UserRole(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('capabilities', 'display_name', 'is_restricted', 'name')
    capabilities = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='capabilities')
    display_name = sgqlc.types.Field(String, graphql_name='displayName')
    is_restricted = sgqlc.types.Field(Boolean, graphql_name='isRestricted')
    name = sgqlc.types.Field(String, graphql_name='name')


class UserToCommentConnection(sgqlc.types.relay.Connection, CommentConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class UserToCommentConnectionEdge(sgqlc.types.Type, CommentConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class UserToCommentConnectionPageInfo(sgqlc.types.Type, CommentConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class UserToEnqueuedScriptConnection(sgqlc.types.relay.Connection, EnqueuedScriptConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class UserToEnqueuedScriptConnectionEdge(sgqlc.types.Type, EnqueuedScriptConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class UserToEnqueuedScriptConnectionPageInfo(sgqlc.types.Type, EnqueuedScriptConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class UserToEnqueuedStylesheetConnection(sgqlc.types.relay.Connection, EnqueuedStylesheetConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class UserToEnqueuedStylesheetConnectionEdge(sgqlc.types.Type, EnqueuedStylesheetConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class UserToEnqueuedStylesheetConnectionPageInfo(sgqlc.types.Type, EnqueuedStylesheetConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class UserToEventConnection(sgqlc.types.relay.Connection, EventConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class UserToEventConnectionEdge(sgqlc.types.Type, EventConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class UserToEventConnectionPageInfo(sgqlc.types.Type, EventConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class UserToJobConnection(sgqlc.types.relay.Connection, JobConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class UserToJobConnectionEdge(sgqlc.types.Type, JobConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class UserToJobConnectionPageInfo(sgqlc.types.Type, JobConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class UserToMediaItemConnection(sgqlc.types.relay.Connection, MediaItemConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class UserToMediaItemConnectionEdge(sgqlc.types.Type, MediaItemConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class UserToMediaItemConnectionPageInfo(sgqlc.types.Type, MediaItemConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class UserToOrganizerConnection(sgqlc.types.relay.Connection, OrganizerConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class UserToOrganizerConnectionEdge(sgqlc.types.Type, OrganizerConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class UserToOrganizerConnectionPageInfo(sgqlc.types.Type, OrganizerConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class UserToPageConnection(sgqlc.types.relay.Connection, PageConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class UserToPageConnectionEdge(sgqlc.types.Type, PageConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class UserToPageConnectionPageInfo(sgqlc.types.Type, PageConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class UserToPartnerConnection(sgqlc.types.relay.Connection, PartnerConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class UserToPartnerConnectionEdge(sgqlc.types.Type, PartnerConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class UserToPartnerConnectionPageInfo(sgqlc.types.Type, PartnerConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class UserToPostConnection(sgqlc.types.relay.Connection, PostConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class UserToPostConnectionEdge(sgqlc.types.Type, PostConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class UserToPostConnectionPageInfo(sgqlc.types.Type, PostConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class UserToRevisionsConnection(sgqlc.types.relay.Connection, ContentNodeConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class UserToRevisionsConnectionEdge(sgqlc.types.Type, ContentNodeConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class UserToRevisionsConnectionPageInfo(sgqlc.types.Type, ContentNodeConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class UserToUserRoleConnection(sgqlc.types.relay.Connection, UserRoleConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class UserToUserRoleConnectionEdge(sgqlc.types.Type, UserRoleConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class UserToUserRoleConnectionPageInfo(sgqlc.types.Type, UserRoleConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class UserToVenueConnection(sgqlc.types.relay.Connection, VenueConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class UserToVenueConnectionEdge(sgqlc.types.Type, VenueConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class UserToVenueConnectionPageInfo(sgqlc.types.Type, VenueConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class Venue(sgqlc.types.Type, Node, ContentNode, UniformResourceIdentifiable, DatabaseIdentifier, NodeWithTemplate, NodeWithTitle, NodeWithContentEditor, NodeWithAuthor, NodeWithFeaturedImage, NodeWithExcerpt, NodeWithRevisions):
    __schema__ = schema
    __field_names__ = ('address', 'city', 'country', 'has_password', 'linked_data', 'password', 'phone', 'province', 'revisions', 'show_map', 'show_map_link', 'state', 'state_province', 'url', 'zip')
    address = sgqlc.types.Field(String, graphql_name='address')
    city = sgqlc.types.Field(String, graphql_name='city')
    country = sgqlc.types.Field(String, graphql_name='country')
    has_password = sgqlc.types.Field(Boolean, graphql_name='hasPassword')
    linked_data = sgqlc.types.Field(VenueLinkedData, graphql_name='linkedData')
    password = sgqlc.types.Field(String, graphql_name='password')
    phone = sgqlc.types.Field(String, graphql_name='phone')
    province = sgqlc.types.Field(String, graphql_name='province')
    revisions = sgqlc.types.Field('VenueToRevisionConnection', graphql_name='revisions', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('where', sgqlc.types.Arg(VenueToRevisionConnectionWhereArgs, graphql_name='where', default=None)),
))
    )
    show_map = sgqlc.types.Field(Boolean, graphql_name='showMap')
    show_map_link = sgqlc.types.Field(Boolean, graphql_name='showMapLink')
    state = sgqlc.types.Field(String, graphql_name='state')
    state_province = sgqlc.types.Field(String, graphql_name='stateProvince')
    url = sgqlc.types.Field(String, graphql_name='url')
    zip = sgqlc.types.Field(String, graphql_name='zip')


class VenueToParentConnectionEdge(sgqlc.types.Type, OneToOneConnection, Edge, VenueConnectionEdge):
    __schema__ = schema
    __field_names__ = ()


class VenueToPreviewConnectionEdge(sgqlc.types.Type, OneToOneConnection, Edge, VenueConnectionEdge):
    __schema__ = schema
    __field_names__ = ()


class VenueToRevisionConnection(sgqlc.types.relay.Connection, VenueConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class VenueToRevisionConnectionEdge(sgqlc.types.Type, VenueConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class VenueToRevisionConnectionPageInfo(sgqlc.types.Type, VenueConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()


class VenueToVenueConnection(sgqlc.types.relay.Connection, VenueConnection, Connection):
    __schema__ = schema
    __field_names__ = ()


class VenueToVenueConnectionEdge(sgqlc.types.Type, VenueConnectionEdge, Edge):
    __schema__ = schema
    __field_names__ = ()


class VenueToVenueConnectionPageInfo(sgqlc.types.Type, VenueConnectionPageInfo, WPPageInfo, PageInfo):
    __schema__ = schema
    __field_names__ = ()



########################################################################
# Unions
########################################################################
class MenuItemObjectUnion(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (Post, Page, Job, Partner, Event, Category, Tag, ContractKind, Jobmode, Occupationkind, EventsCategory)



########################################################################
# Schema Entry Points
########################################################################
schema.query_type = RootQuery
schema.mutation_type = RootMutation
schema.subscription_type = None

