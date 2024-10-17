from django.shortcuts import render
#Mis importaciones - Richy
import json
import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.views import APIView
from .serializers import EmisionesSerializer
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Emisiones
from .serializers import EmisionesSerializer

def accordions_collapse (request): 
    return render(request, 'accordions-collapse.html')
def add_products (request): 
    return render(request, 'add-products.html')
def alerts  (request): 
    return render(request, 'alerts.html')
def apex_area_charts (request): 
    return render(request, 'apex-area-charts.html')
def apex_bar_charts (request): 
    return render(request, 'apex-bar-charts.html')
def apex_boxplot_charts (request): 
    return render(request, 'apex-boxplot-charts.html')
def apex_bubble_charts (request): 
    return render(request, 'apex-bubble-charts.html')
def apex_candlestick_charts (request): 
    return render(request, 'apex-candlestick-charts.html')
def apex_column_charts (request): 
    return render(request, 'apex-column-charts.html')
def apex_funnel_charts (request): 
    return render(request, 'apex-funnel-charts.html')
def apex_heatmap_charts (request): 
    return render(request, 'apex-heatmap-charts.html')
def apex_line_charts (request): 
    return render(request, 'apex-line-charts.html')
def apex_mixed_charts (request): 
    return render(request, 'apex-mixed-charts.html')
def apex_pie_charts (request): 
    return render(request, 'apex-pie-charts.html')
def apex_polararea_charts (request): 
    return render(request, 'apex-polararea-charts.html')
def apex_radar_charts (request): 
    return render(request, 'apex-radar-charts.html')
def apex_radialbar_charts (request): 
    return render(request, 'apex-radialbar-charts.html')
def apex_rangearea_charts (request): 
    return render(request, 'apex-rangearea-charts.html')
def apex_scatter_charts (request): 
    return render(request, 'apex-scatter-charts.html')
def apex_timeline_charts (request): 
    return render(request, 'apex-timeline-charts.html')
def apex_treemap_charts (request): 
    return render(request, 'apex-treemap-charts.html')
def avatars (request): 
    return render(request, 'avatars.html')
def badges (request): 
    return render(request, 'badges.html')
def blog_create (request): 
    return render(request, 'blog-create.html')
def blog_details (request): 
    return render(request, 'blog-details.html')
def blog (request): 
    return render(request, 'blog.html')
def borders (request): 
    return render(request, 'borders.html')
def breadcrumbs (request): 
    return render(request, 'breadcrumbs.html')
def breakpoints (request): 
    return render(request, 'breakpoints.html')
def buttongroups (request): 
    return render(request, 'buttongroups.html')
def buttons (request): 
    return render(request, 'buttons.html')
def cards (request): 
    return render(request, 'cards.html')
def carousel (request): 
    return render(request, 'carousel.html')
def cart (request): 
    return render(request, 'cart.html')
def chartjs_charts (request): 
    return render(request, 'chartjs-charts.html')
def chat (request): 
    return render(request, 'chat.html')
def checkout (request): 
    return render(request, 'checkout.html')
def colors (request): 
    return render(request, 'colors.html')
def columns (request): 
    return render(request, 'columns.html')
def coming_soon (request): 
    return render(request, 'coming-soon.html')
def contact_us (request): 
    return render(request, 'contact-us.html')
def contacts (request): 
    return render(request, 'contacts.html')
def createpassword_basic (request): 
    return render(request, 'createpassword-basic.html')
def createpassword_cover (request): 
    return render(request, 'createpassword-cover.html')
def crm_companies (request): 
    return render(request, 'crm-companies.html')
def crm_contacts (request): 
    return render(request, 'crm-contacts.html')
def crm_deals (request): 
    return render(request, 'crm-deals.html')
def crm_leads (request): 
    return render(request, 'crm-leads.html')
def crypto_buy_sell (request): 
    return render(request, 'crypto-buy-sell.html')
def crypto_currency_exchange (request): 
    return render(request, 'crypto-currency-exchange.html')
def crypto_marketcap (request): 
    return render(request, 'crypto-marketcap.html')
def crypto_transactions (request): 
    return render(request, 'crypto-transactions.html')
def crypto_wallet (request): 
    return render(request, 'crypto-wallet.html')
def data_tables (request): 
    return render(request, 'data-tables.html')
def draggable_cards (request): 
    return render(request, 'draggable-cards.html')
def dropdowns (request): 
    return render(request, 'dropdowns.html')
def echarts (request): 
    return render(request, 'echarts.html')
def edit_products (request): 
    return render(request, 'edit-products.html')
def empty_page (request): 
    return render(request, 'empty-page.html')
def error401 (request): 
    return render(request, 'error401.html')
def error404 (request): 
    return render(request, 'error404.html')
def error500 (request): 
    return render(request, 'error500.html')
def faqs (request): 
    return render(request, 'faqs.html')
def file_manager (request): 
    return render(request, 'file-manager.html')
def flex (request): 
    return render(request, 'flex.html')
def floating_labels (request): 
    return render(request, 'floating-labels.html')
def form_advanced (request): 
    return render(request, 'form-advanced.html')
def form_check_radios (request): 
    return render(request, 'form-check-radios.html')
def form_color_pickers (request): 
    return render(request, 'form-color-pickers.html')
def form_datetime_pickers (request): 
    return render(request, 'form-datetime-pickers.html')
def form_file_uploads (request): 
    return render(request, 'form-file-uploads.html')
def form_input_groups (request): 
    return render(request, 'form-input-groups.html')
def form_input_masks (request): 
    return render(request, 'form-input-masks.html')
def form_inputs (request): 
    return render(request, 'form-inputs.html')
def form_layouts (request): 
    return render(request, 'form-layouts.html')
def form_range (request): 
    return render(request, 'form-range.html')
def form_select (request): 
    return render(request, 'form-select.html')
def form_select2 (request): 
    return render(request, 'form-select2.html')
def form_validations (request): 
    return render(request, 'form-validations.html')
def form_wizards (request): 
    return render(request, 'form-wizards.html')
def full_calendar (request): 
    return render(request, 'full-calendar.html')
def gallery (request): 
    return render(request, 'gallery.html')
def google_maps (request): 
    return render(request, 'google-maps.html')
def grid_tables (request): 
    return render(request, 'grid-tables.html')
def gutters (request): 
    return render(request, 'gutters.html')
def helpers (request): 
    return render(request, 'helpers.html')
def icons (request): 
    return render(request, 'icons.html')
def index (request): 
    return render(request, 'index.html')
def index2 (request): 
    return render(request, 'index2.html')
def index3 (request): 
    return render(request, 'index3.html')
def index4 (request): 
    return render(request, 'index4.html')
def index5 (request): 
    return render(request, 'index5.html')
def index6 (request): 
    return render(request, 'index6.html')
def index7 (request): 
    return render(request, 'index7.html')
def index8 (request): 
    return render(request, 'index8.html')
def index9 (request): 
    return render(request, 'index9.html')
def index10 (request): 
    return render(request, 'index10.html')
def index11 (request): 
    return render(request, 'index11.html')
def index12 (request): 
    return render(request, 'index12.html')
def images_figures (request): 
    return render(request, 'images-figures.html')
def invoice_create (request): 
    return render(request, 'invoice-create.html')
def invoice_details (request): 
    return render(request, 'invoice-details.html')
def invoice_list (request): 
    return render(request, 'invoice-list.html')
def job_candidate_details (request): 
    return render(request, 'job-candidate-details.html')
def job_candidate_search (request): 
    return render(request, 'job-candidate-search.html')
def job_company_search (request): 
    return render(request, 'job-company-search.html')
def job_details (request): 
    return render(request, 'job-details.html')
def job_list (request): 
    return render(request, 'job-list.html')
def job_post (request): 
    return render(request, 'job-post.html')
def job_search (request): 
    return render(request, 'job-search.html')
def landing_jobs (request): 
    return render(request, 'landing-jobs.html')
def landing (request): 
    return render(request, 'landing.html')
def loaders (request): 
    return render(request, 'loaders.html')
def leaflet_maps (request): 
    return render(request, 'leaflet-maps.html')
def links_interactions (request): 
    return render(request, 'links-interactions.html')
def listgroups (request): 
    return render(request, 'listgroups.html')
def lockscreen_basic (request): 
    return render(request, 'lockscreen-basic.html')
def lockscreen_cover (request): 
    return render(request, 'lockscreen-cover.html')
def mail_settings (request): 
    return render(request, 'mail-settings.html')
def mail (request): 
    return render(request, 'mail.html')
def modals_closes (request): 
    return render(request, 'modals-closes.html')
def more (request): 
    return render(request, 'more.html')
def navbars (request): 
    return render(request, 'navbars.html')
def navs_tabs (request): 
    return render(request, 'navs-tabs.html')
def nft_create (request): 
    return render(request, 'nft-create.html')
def nft_details (request): 
    return render(request, 'nft-details.html')
def nft_live_auction (request): 
    return render(request, 'nft-live-auction.html')
def nft_marketplace (request): 
    return render(request, 'nft-marketplace.html')
def nft_wallet_integration (request): 
    return render(request, 'nft-wallet-integration.html')
def notifications (request): 
    return render(request, 'notifications.html')
def object_fit (request): 
    return render(request, 'object-fit.html')
def offcanvas (request): 
    return render(request, 'offcanvas.html')
def order_details (request): 
    return render(request, 'order-details.html')
def orders (request): 
    return render(request, 'orders.html')
def paginations (request): 
    return render(request, 'paginations.html')
def placeholders (request): 
    return render(request, 'placeholders.html')
def popovers (request): 
    return render(request, 'popovers.html')
def positions (request): 
    return render(request, 'positions.html')
def pricing (request): 
    return render(request, 'pricing.html')
def product_details (request): 
    return render(request, 'product-details.html')
def product_list (request): 
    return render(request, 'product-list.html')
def products (request): 
    return render(request, 'products.html')
def profile_settings (request): 
    return render(request, 'profile-settings.html')
def profile (request): 
    return render(request, 'profile.html')
def progress (request): 
    return render(request, 'progress.html')
def projects_create (request): 
    return render(request, 'projects-create.html')
def projects_list (request): 
    return render(request, 'projects-list.html')
def projects_overview (request): 
    return render(request, 'projects-overview.html')
def quill_editor (request): 
    return render(request, 'quill-editor.html')
def ratings (request): 
    return render(request, 'ratings.html')
def resetpassword_basic (request): 
    return render(request, 'resetpassword-basic.html')
def resetpassword_cover (request): 
    return render(request, 'resetpassword-cover.html')
def reviews (request): 
    return render(request, 'reviews.html')
def ribbons (request): 
    return render(request, 'ribbons.html')
def scrollspy (request): 
    return render(request, 'scrollspy.html')
def search_page (request): 
    return render(request, 'search-page.html')
def signin_basic (request): 
    return render(request, 'signin-basic.html')
def signin_cover (request): 
    return render(request, 'signin-cover.html')
def signup_basic (request): 
    return render(request, 'signup-basic.html')
def signup_cover (request): 
    return render(request, 'signup-cover.html')
def sortable_list (request): 
    return render(request, 'sortable-list.html')
def spinners (request): 
    return render(request, 'spinners.html')
def sweet_alerts (request): 
    return render(request, 'sweet-alerts.html')
def swiperjs (request): 
    return render(request, 'swiperjs.html')
def tables (request): 
    return render(request, 'tables.html')
def task_details (request): 
    return render(request, 'task-details.html')
def task_kanban_board (request): 
    return render(request, 'task-kanban-board.html')
def task_list_view (request): 
    return render(request, 'task-list-view.html')
def team (request): 
    return render(request, 'team.html')
def terms_conditions (request): 
    return render(request, 'terms-conditions.html')
def timeline (request): 
    return render(request, 'timeline.html')
def toasts (request): 
    return render(request, 'toasts.html')
def todo_list (request): 
    return render(request, 'todo-list.html')
def tooltips (request): 
    return render(request, 'tooltips.html')
def twostep_verification_basic (request): 
    return render(request, 'twostep-verification-basic.html')
def twostep_verification_cover (request): 
    return render(request, 'twostep-verification-cover.html')
def typography (request): 
    return render(request, 'typography.html')
def under_maintenance (request): 
    return render(request, 'under-maintenance.html')
def vector_maps (request): 
    return render(request, 'vector-maps.html')
def canada (request): 
    return render(request, 'canada.html')
def russia (request): 
    return render(request, 'russia.html')
def spain (request): 
    return render(request, 'spain.html')
def mexico (request): 
    return render(request, 'mexico.html')
def italy (request): 
    return render(request, 'italy.html')
def usa (request): 
    return render(request, 'usa.html')
def countries (request): 
    return render(request, 'countries.html')
def widgets (request): 
    return render(request, 'widgets.html')
def wishlist (request): 
    return render(request, 'wishlist.html')


@csrf_exempt
def get_gemini_answer(request):
    if request.method == 'POST':
        # Cargar el cuerpo de la solicitud como JSON
        try:
            data = json.loads(request.body)
            question = data.get('question')  # Obtener 'question' del JSON

            if not question:
                return JsonResponse({'error': 'La pregunta es obligatoria'}, status=400)

            api_url = "https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key=AIzaSyB-BPYppGfIWDCZuiDSRrQpJdNKxO-RRP0"
            headers = {
                'Content-Type': 'application/json',
            }
            payload = {  # Usar 'payload' para mantener la estructura correcta
                "contents": [
                    {
                        "role": "user",
                        "parts": [{"text": question}]
                    }
                ]
            }

            response = requests.post(api_url, json=payload, headers=headers)

            if response.status_code == 200:
                return JsonResponse(response.json())
            else:
                return JsonResponse({'error': 'Error al obtener una respuesta válida de la API'}, status=response.status_code)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'El cuerpo de la solicitud no es JSON válido'}, status=400)

    return JsonResponse({'error': 'Método no permitido'}, status=405)
#Mis modificaciones (Richy backend y generación de api rest)

class EmisionesAPIView(APIView):
    def get(self, request):
        # Obtén todos los registros de la base de datos
        emisiones = Emisiones.objects.all()  # Cargar los datos desde la base de datos
        
        # Serializa los datos
        serializer = EmisionesSerializer(emisiones, many=True)
        
        # Retorna la respuesta JSON
        return Response(serializer.data)
    