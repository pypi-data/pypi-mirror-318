from typing import Optional

from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponse
from django.template.loader import select_template
from django.views import View
from django.views.generic.base import ContextMixin
from django_xhtml2pdf.utils import generate_pdf


class PDFView(ContextMixin, View):
    """A base class that renders requests as PDF files.

    All views that render a PDF must inherit from this base class.

    Usage and interface is quite similar to Django's built-in views. Template
    context data can be defined via ``get_context_data`` just like with
    Django's ``TemplateView`` subclasses.

    The following additional attributes allow further customising behaviour of
    subclasses. These may be overridden by either an attribute or a property:

    .. autoattribute:: allow_force_html

        Allow forcing this view to return a rendered HTML response, rather than a PDF
        response.  If ``True``, any requests with the URL parameter ``html=true`` will
        be rendered as plain HTML. This can be useful for debugging, but also allows
        reusing the same view for exposing both PDFs and HTML.

    .. autoattribute:: prompt_download

        If ``True``, users will be prompted to download the PDF file, rather than have
        it rendered by their browsers.

        This is achieved by setting the "Content-Disposition" HTTP header. If this
        attribute is ``True``, then :attr:`~download_name` should be defined

    .. autoattribute:: download_name

        When ``prompt_download`` is set to ``True``, browsers will be instructed to
        prompt users to download the file, rather than render it.

        In these cases, a default filename is presented. If you need custom filenames,
        you may override this attribute with a property:

        .. code:: python

            @property
            def download_name(self) -> str:
                return f"document_{self.request.kwargs['pk']}.pdf"

        This attribute has no effect if ``prompt_download = False``.
    """

    allow_force_html: bool = True
    prompt_download: bool = False
    download_name: Optional[str] = None

    def get_download_name(self) -> str:
        """Return the default filename when this file is downloaded."""
        if self.download_name is None:
            raise ImproperlyConfigured(
                f"{self.__class__.__name__} with 'prompt_download=True' requires a definition " "of 'download_name'."
            )
        return self.download_name

    def render(self, request, template, context) -> HttpResponse:
        """Returns a response.

        By default, this will contain the rendered PDF, but if both ``allow_force_html``
        is ``True`` and the querystring ``html=true`` was set it will return a plain
        HTML.
        """
        if self.allow_force_html and self.request.GET.get('html', False):
            html = select_template([template]).render(context)
            return HttpResponse(html)

        response = HttpResponse(content_type='application/pdf')
        if self.prompt_download:
            filename = self.get_download_name()
            response['Content-Disposition'] = f'attachment; filename="{filename}"'

        generate_pdf(template, file_object=response, context=context)
        return response

    def get(self, request, *args, **kwargs) -> HttpResponse:
        context = self.get_context_data(*args, **kwargs)
        template = self.get_template_names()
        if type(template) is list:
            template = template[0]
        return self.render(
            request=request,
            template=template,
            context=context,
        )
