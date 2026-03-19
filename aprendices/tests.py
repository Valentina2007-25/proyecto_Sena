from django.db import IntegrityError
from django.test import Client, TestCase
from django.urls import reverse

from aprendices.forms import AprendizForm
from aprendices.models import Aprendiz


class AprendizTestBase(TestCase):
    """Clase base con un aprendiz de prueba reutilizable."""

    def setUp(self):
        self.aprendiz = Aprendiz.objects.create(
            documento_identidad="1234567890",
            nombre="Pepito",
            apellido="Perez",
            telefono="3101234567",
            correo="pepitoperez@sena.edu.co",
            fecha_nacimiento="2000-01-15",
            ciudad="Sogamoso",
            programa="Analisis y Desarrollo de Software",
        )
        self.client = Client()


class AprendizModelTest(AprendizTestBase):
    def test_aprendiz_se_crea_correctamente(self):
        aprendiz = Aprendiz.objects.get(documento_identidad="1234567890")
        self.assertEqual(aprendiz.nombre, "Pepito")
        self.assertEqual(aprendiz.apellido, "Perez")
        self.assertEqual(aprendiz.ciudad, "Sogamoso")

    def test_str_retorna_nombre_y_apellido(self):
        self.assertEqual(str(self.aprendiz), "Pepito Perez")

    def test_nombre_completo_concatena_correctamente(self):
        self.assertEqual(self.aprendiz.nombre_completo(), "Pepito Perez")

    def test_documento_identidad_debe_ser_unico(self):
        with self.assertRaises(IntegrityError):
            Aprendiz.objects.create(
                documento_identidad="1234567890",
                nombre="Otro",
                apellido="Usuario",
                fecha_nacimiento="1999-05-20",
                programa="Sistemas",
            )

    def test_campos_opcionales_aceptan_null(self):
        aprendiz_minimo = Aprendiz.objects.create(
            documento_identidad="9999999999",
            nombre="Maria",
            apellido="Gomez",
            fecha_nacimiento="2001-03-10",
            programa="Contabilidad",
        )
        self.assertIsNone(aprendiz_minimo.telefono)
        self.assertIsNone(aprendiz_minimo.correo)
        self.assertIsNone(aprendiz_minimo.ciudad)


class AprendizFormTest(TestCase):
    def get_datos_validos(self):
        return {
            "documento_identidad": "1098765432",
            "nombre": "Laura",
            "apellido": "Garcia",
            "telefono": "3209876543",
            "correo": "laura@sena.edu.co",
            "fecha_nacimiento": "2002-07-20",
            "ciudad": "Medellin",
        }

    def test_formulario_valido_con_datos_correctos(self):
        form = AprendizForm(data=self.get_datos_validos())
        self.assertTrue(form.is_valid(), msg=f"Errores: {form.errors}")

    def test_documento_con_letras_es_invalido(self):
        datos = self.get_datos_validos()
        datos["documento_identidad"] = "ABC123456"
        form = AprendizForm(data=datos)
        self.assertFalse(form.is_valid())
        self.assertIn("documento_identidad", form.errors)

    def test_telefono_con_letras_es_invalido(self):
        datos = self.get_datos_validos()
        datos["telefono"] = "abc1234567"
        form = AprendizForm(data=datos)
        self.assertFalse(form.is_valid())
        self.assertIn("telefono", form.errors)

    def test_telefono_con_menos_de_10_digitos_es_invalido(self):
        datos = self.get_datos_validos()
        datos["telefono"] = "31012345"
        form = AprendizForm(data=datos)
        self.assertFalse(form.is_valid())
        self.assertIn("telefono", form.errors)

    def test_correo_invalido_es_rechazado(self):
        datos = self.get_datos_validos()
        datos["correo"] = "esto_no_es_un_correo"
        form = AprendizForm(data=datos)
        self.assertFalse(form.is_valid())
        self.assertIn("correo", form.errors)

    def test_campos_obligatorios_vacios_invalidan_formulario(self):
        form = AprendizForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn("documento_identidad", form.errors)
        self.assertIn("nombre", form.errors)
        self.assertIn("apellido", form.errors)


class AprendizViewTest(AprendizTestBase):
    def test_lista_aprendices_responde_200(self):
        url = reverse("aprendices:lista_aprendices")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_lista_aprendices_usa_template_correcto(self):
        url = reverse("aprendices:lista_aprendices")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "lista_aprendices.html")

    def test_lista_aprendices_contiene_el_aprendiz_creado(self):
        url = reverse("aprendices:lista_aprendices")
        response = self.client.get(url)
        self.assertContains(response, "Pepito")
        self.assertContains(response, "Perez")

    def test_detalle_aprendiz_existente_responde_200(self):
        url = reverse(
            "aprendices:detalle_aprendiz",
            kwargs={"id_aprendiz": self.aprendiz.id},
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "1234567890")

    def test_crear_aprendiz_con_datos_validos_redirige(self):
        url = reverse("aprendices:crear_aprendiz")
        datos = {
            "documento_identidad": "5555555555",
            "nombre": "Carlos",
            "apellido": "Lopez",
            "telefono": "3001112233",
            "correo": "carlos@test.com",
            "fecha_nacimiento": "1999-11-05",
            "ciudad": "Cali",
        }
        response = self.client.post(url, data=datos)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            Aprendiz.objects.filter(documento_identidad="5555555555").exists()
        )

    def test_crear_aprendiz_con_datos_invalidos_no_redirige(self):
        url = reverse("aprendices:crear_aprendiz")
        datos_invalidos = {
            "documento_identidad": "INVALIDO",
            "nombre": "",
            "apellido": "Test",
            "fecha_nacimiento": "2000-01-01",
        }
        response = self.client.post(url, data=datos_invalidos)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(
            Aprendiz.objects.filter(documento_identidad="INVALIDO").exists()
        )

    def test_editar_aprendiz_actualiza_datos(self):
        url = reverse(
            "aprendices:editar_aprendiz",
            kwargs={"aprendiz_id": self.aprendiz.id},
        )
        datos_actualizados = {
            "documento_identidad": "1234567890",
            "nombre": "Juan Carlos",
            "apellido": "Perez",
            "telefono": "3001234567",
            "correo": "juan@test.com",
            "fecha_nacimiento": "2000-01-15",
            "ciudad": "Barranquilla",
        }
        response = self.client.post(url, data=datos_actualizados)
        self.assertEqual(response.status_code, 302)
        self.aprendiz.refresh_from_db()
        self.assertEqual(self.aprendiz.nombre, "Juan Carlos")
        self.assertEqual(self.aprendiz.ciudad, "Barranquilla")

    def test_eliminar_aprendiz_lo_borra_de_la_bd(self):
        aprendiz_id = self.aprendiz.id
        url = reverse(
            "aprendices:eliminar_aprendiz",
            kwargs={"aprendiz_id": aprendiz_id},
        )
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Aprendiz.objects.filter(id=aprendiz_id).exists())


class AprendizURLTest(TestCase):
    def test_url_lista_aprendices_resuelve_correctamente(self):
        url = reverse("aprendices:lista_aprendices")
        self.assertEqual(url, "/aprendices/lista/")

    def test_url_crear_aprendiz_resuelve_correctamente(self):
        url = reverse("aprendices:crear_aprendiz")
        self.assertEqual(url, "/aprendices/crear/")

    def test_url_detalle_aprendiz_resuelve_correctamente(self):
        url = reverse("aprendices:detalle_aprendiz", kwargs={"id_aprendiz": 1})
        self.assertEqual(url, "/aprendices/1/")

    def test_url_editar_aprendiz_resuelve_correctamente(self):
        url = reverse("aprendices:editar_aprendiz", kwargs={"aprendiz_id": 1})
        self.assertEqual(url, "/aprendices/1/editar/")

    def test_url_eliminar_aprendiz_resuelve_correctamente(self):
        url = reverse("aprendices:eliminar_aprendiz", kwargs={"aprendiz_id": 1})
        self.assertEqual(url, "/aprendices/1/eliminar/")
