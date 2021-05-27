def diagSintoma(paciente: dict) -> dict:
    resultado = {'id_diagnostico':paciente['id_diagnostico'],'resultado':'','estado':''}
    if paciente["diag_ta"] == "Si":
        if paciente["diag_pa"] == "Si":
            if paciente["diag_do"] == "Si":
                if paciente["diag_dg"] == "Si":
                    if paciente["diag_dc"] == "Si":
                        resultado["resultado"] = "Covid 19"
                        resultado["estado"] = True
                    else:
                        resultado["resultado"] = 'Presencia de síntomas'
                        resultado["estado"] = False
                else:
                    resultado["resultado"] = 'Presencia de síntomas'
                    resultado["estado"] = False
            else:
                resultado["resultado"] = 'Presencia de síntomas'
                resultado["estado"] = False
        else:
            if paciente["diag_do"] == "Si":
                resultado["resultado"] = 'Presencia de síntomas'
                resultado["estado"] = False
            else:
                if paciente["diag_dg"] == "Si":
                    if paciente["diag_dc"] == "Si":
                        resultado["resultado"] = "gripa"
                        resultado["estado"] = True
                    else:
                        resultado["resultado"] = 'Presencia de síntomas'
                        resultado["estado"] = False
                else:
                    resultado["resultado"] = 'Presencia de síntomas'
                    resultado["estado"] = False
    else:
        if paciente['diag_pa'] == 'Si':
            if paciente['diag_do']:
                if paciente['diag_dg']:
                    if paciente['diag_dc']:
                        resultado["resultado"] = 'Presencia de síntomas'
                        resultado["estado"] = False
                    else:
                        resultado["resultado"] = 'Otitis'
                        resultado["estado"] = True
                else:
                    resultado["resultado"] = 'Presencia de síntomas'
                    resultado["estado"] = False
            else:
                resultado["resultado"] = 'Presencia de síntomas'
                resultado["estado"] = False
        else:
            if paciente['diag_do'] == 'Si' and paciente['diag_dg'] == 'Si' and paciente['diag_dc'] == 'Si':
                resultado["resultado"] = 'Presencia de síntomas'
                resultado["estado"] = False
            else:
                resultado["resultado"] = 'No tiene síntomas'
                resultado["estado"] = False
    return resultado
