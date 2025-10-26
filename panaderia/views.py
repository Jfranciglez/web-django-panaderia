from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def productos(request):
    productos = [
        {
            "categoria": "Panes Artesanales",
            "items": [
                {
                    "nombre": "Baguette Tradicional",
                    "descripcion": "Pan francés de corteza crujiente y miga ligera.",
                    "precio": 1.50
                },
                {
                    "nombre": "Pan Integral con Semillas",
                    "descripcion": "Rico en fibra, con mezcla de girasol, lino y sésamo.",
                    "precio": 2.00
                },
                {
                    "nombre": "Pan de Centeno Rústico",
                    "descripcion": "Elaborado con masa madre y harina de centeno.",
                    "precio": 2.20
                },
            ]
        },
        {
            "categoria": "Bollería y Dulces",
            "items": [
                {
                    "nombre": "Croissant de Mantequilla",
                    "descripcion": "Hojaldre clásico, recién horneado, dorado y crujiente.",
                    "precio": 1.20
                },
                {
                    "nombre": "Napolitana de Chocolate",
                    "descripcion": "Masa de hojaldre rellena de crema y chocolate fundido.",
                    "precio": 1.50
                },
                {
                    "nombre": "Ensaimada Mallorquina",
                    "descripcion": "Dulce esponjoso con azúcar glas y toque de limón.",
                    "precio": 1.80
                },
            ]
        },
        {
            "categoria": "Pasteles y Tartas",
            "items": [
                {
                    "nombre": "Tarta de Queso",
                    "descripcion": "Suave y cremosa, con base de galleta y aroma a vainilla.",
                    "precio": 3.00
                },
                {
                    "nombre": "Pastel de Zanahoria",
                    "descripcion": "Con nueces, canela y cobertura de queso crema.",
                    "precio": 3.20
                },
                {
                    "nombre": "Brownie de Chocolate",
                    "descripcion": "Denso, húmedo y con trozos de chocolate negro.",
                    "precio": 2.80
                },
            ]
        },
        {
            "categoria": "Galletas y Snacks",
            "items": [
                {
                    "nombre": "Galletas de Avena y Miel",
                    "descripcion": "Crujientes y saludables, perfectas para acompañar el café.",
                    "precio": 1.00
                },
                {
                    "nombre": "Galletas con Chispas de Chocolate",
                    "descripcion": "Clásicas, con extra de trocitos de chocolate.",
                    "precio": 1.20
                },
                {
                    "nombre": "Palmeritas de Hojaldre",
                    "descripcion": "Crujientes, caramelizadas y hechas con mantequilla pura.",
                    "precio": 1.00
                },
            ]
        },
        {
            "categoria": "Bebidas",
            "items": [
                {
                    "nombre": "Café Espresso",
                    "descripcion": "Preparado con granos seleccionados, sabor intenso.",
                    "precio": 1.20
                },
                {
                    "nombre": "Té Verde Natural",
                    "descripcion": "Infusión ligera y antioxidante, servida caliente o fría.",
                    "precio": 1.50
                },
                {
                    "nombre": "Chocolate Caliente",
                    "descripcion": "Espeso y cremoso, elaborado con cacao puro.",
                    "precio": 1.80
                },
            ]
        }
    ]
    context = {"productos": productos,}
    return render(request, "productos.html", context)

def ofertas(request):
    ofertas = {
            "ofertas_diarias": [
                {
                    "titulo": "Combo Desayuno — Café + Croissant",
                    "descripcion": "Perfecto para empezar el día.",
                    "precio": 2.50
                },
                {
                    "titulo": "Hora Feliz del Pan — 2×1",
                    "descripcion": "De 17:00 a 19:00 — panes artesanales.",
                    "precio": "2x1"
                },
                {
                    "titulo": "Pan del Día — 20% off",
                    "descripcion": "Descuento en la hornada del día.",
                    "precio": "-20%"
                },
            ],
            "promociones_semanales": [
                {
                    "titulo": "Miércoles Dulce — 3+1",
                    "descripcion": "Compra 3 pasteles y llévate el 4.º gratis.",
                    "precio": "4.º gratis"
                },
                {
                    "titulo": "Jueves Familiar — 10% off",
                    "descripcion": "En compras mayores a $10.",
                    "precio": "-10%"
                },
                {
                    "titulo": "Fin de Semana Enigmático — 15% off",
                    "descripcion": "15% en tortas y postres los sábados y domingos.",
                    "precio": "-15%"
                },
            ],
            "ofertas_especiales": [
                {
                    "titulo": "Tarjeta de Fidelidad",
                    "descripcion": "A la 10.ª compra, ¡una baguette gratis!",
                    "precio": "10→Gratis"
                },
                {
                    "titulo": "Cumpleaños Feliz",
                    "descripcion": "Mini pastel gratuito presentando ID.",
                    "precio": "Gratis"
                },
                {
                    "titulo": "Pan Solidario",
                    "descripcion": "Llévate una pieza extra para donar.",
                    "precio": "-"
                },
            ]
        }

    context = {"ofertas": ofertas}
    return render(request, "ofertas.html", context)

def contacto(request):
    context = {
        "localizacion": {
            "direccion": "Calle Alegre 88, Málaga, España",
            "latitud": 36.7213028,
            "longitud": -4.4216366
        },
        "contacto": {
            "telefono": 678904352,
            "email": "example@alu.es"
        }
    } #las demas cosas tambien si se repiten mucho las pongo en json como aqui.
    return render(request, "contacto.html", context=context)