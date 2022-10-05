from django.contrib import admin
from .models import Product, Review, Category
from django.utils import timezone
from django.utils.safestring import mark_safe
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from import_export.admin import ImportExportModelAdmin
from products.resources import ReviewResource

# Register your models here.



admin.site.site_title = "Clarusway Title"
admin.site.site_header = "Clarusway Admin Portal" 
admin.site.index_title = "Welcome to Clarusway Admin Portal"


class ReviewInline(admin.TabularInline):  # StackedInline farklı bir görünüm aynı iş
    '''Tabular Inline View for '''
    model = Review
    extra = 1 ## yani ekstra bir tane daha Review alani veriyor.
    classes = ('collapse',) ## Review'lerin kapali olarak gelmesini sagliyor!
    # min_num = 3
    # max_num = 20




class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "create_date", "is_in_stock", "update_date", "added_days_ago", "how_many_reviews", "bring_img_to_list")
    list_editable = ( "is_in_stock", )
    list_display_links = ("name", ) #can't add items in list_editable to here
    list_filter = ("is_in_stock",("create_date", DateTimeRangeFilter))
    ordering = ("name",)
    search_fields = ("name",)
    prepopulated_fields = {'slug' : ('name',)}   # when adding product in admin site
    list_per_page = 25
    date_hierarchy = "update_date"
    # fields = ( "description",("name", "slug"), "is_in_stock") #!fieldset kullandığımız zaman bunu kullanamayız
    inlines = (ReviewInline,)
    readonly_fields = ("bring_image",)

    fieldsets = (
        ("Main Menu", {
            "fields": (
                ('name', 'slug'), "is_in_stock" # to display multiple fields on the same line, wrap those fields in their own tuple
            ),
            # 'classes': ('wide', 'extrapretty'), wide or collapse
        }),
        ('Optionals Settings', {
            "classes" : ("collapse", ),
            "fields" : ("description","categories", "product_img", "bring_image"),
            'description' : "You can use this section for optionals settings"
        })
    )

    # filter_horizontal = ("categories", )
    filter_vertical = ("categories", )



    actions = ("is_in_stock", )
    def is_in_stock(self, request, queryset):
        count = queryset.update(is_in_stock=True)
        self.message_user(request, f"{count} çeşit ürün stoğa eklendi")
        
    is_in_stock.short_description = 'İşaretlenen ürünleri stoğa ekle'


    def added_days_ago(self, product):
        	fark = timezone.now() - product.create_date
        	return fark.days

    # def how_many_reviews(self, product): ## admin panalde tek fark "product" ekleyecegiz.
    #     count = product.reviews.count()
    #     return count

    def bring_img_to_list(self, obj):
        if obj.product_img:
            return mark_safe(f"<img src={obj.product_img.url} width=50 height=50></img>")
        return mark_safe("******")

    bring_img_to_list.short_description = "product_image"



class ReviewAdmin(ImportExportModelAdmin):
    list_display = ('__str__', 'created_date', 'is_released')
    list_per_page = 50
    raw_id_fields = ('product',)
    list_filter = (
        ('product', RelatedDropdownFilter),
    ) 
    resource_class = ReviewResource

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'


admin.site.register(Review, ReviewAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
