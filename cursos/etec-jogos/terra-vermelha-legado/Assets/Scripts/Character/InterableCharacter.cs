using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class InterableCharacter : MonoBehaviour {

    HUDController hud;

    bool interable = false;
    bool info = false;
    public Collider objColl;

    private void Start()
    {
        hud = GameObject.FindGameObjectWithTag("HUD").GetComponent<HUDController>();
    }

    private void Update()
    {
        if (objColl != null)
        {
            if (inputControl() && info && objColl.GetComponentInParent<ConstrucoesInfo>()) VerificaDialogo();
            if (inputControl() && objColl.GetComponent<FrutaItem>()) VerificaFruta();
            if (inputControl() && objColl.GetComponent<DoorInterable>()) VerificaDoor();
            if(inputControl() && objColl.GetComponent<DialogoController>()) verificarDialogoNPC();
        }
    }


    int indexDialogo = 0;
    List<string> dialogo;
    bool dialogoVisivel = false;

    private void verificarDialogoNPC()
    {
        if(!dialogoVisivel) dialogoVisivel = true;

        DialogoTable g = objColl.GetComponent<DialogoController>().dialogo;
        NPCController n = objColl.GetComponent<NPCController>();
        dialogo = g.dialogos;

        if(indexDialogo < dialogo.Count) {
            hud.dialog(true, n.nome, g.dialogos[indexDialogo], null);
            hud.interable(false);
            indexDialogo++;
        } else {
            hud.dialog(false, "", "", null);
            if(!dialogoVisivel) dialogoVisivel = false;
            hud.interable(true, "Falar", null);
            indexDialogo = 0;
        }
    }

    private void VerificaDoor()
    {
        
        DoorInterable g = objColl.GetComponent<DoorInterable>();

		if (g.podeAbrir) {
			if (!g.abrir) {
				g.abrir = true;
				hud.interable ("Fechar");
			} else {
				g.abrir = false;
				hud.interable ("Abrir");
			}
		} else {
			hud.interable ("Trancado");
		}
    }

    private void VerificaFruta()
    {
        FrutasTable g = objColl.GetComponent<FrutaItem>().item;

        hud.mission(true, null, "Inventário", g.nome + " adicionado no iventário de frutas", 10);

        Collider c = objColl;
        objColl = null;
        Destroy(c.gameObject);

        interable = false;
        hud.interable(false);
    }
    
    /// <summary>
    /// Controle do diálogo de informações do jogo
    /// </summary>
    private void VerificaDialogo()
    {
        if (!hud.dialogVisible())
        {
            ConstrucoesInfo g = objColl.GetComponentInParent<ConstrucoesInfo>();

            hud.dialog(true, g.nome, g.descricao, null);
            hud.interable(false);
        }
        else if (hud.dialogVisible())
        {
            hud.dialog(false);
            hud.interable(true);
        }
    }

    /// <summary>
    /// funcao que verifica teclas do jogo
    /// </summary>
    /// <returns>retorna trua caso o interable e a tecla espefífica for prescionada </returns>
    private bool inputControl()
    {
        return interable && Input.GetButtonDown("Atack");
    }

    private void OnTriggerEnter(Collider c)
    {

        if (GetComponentInParent<CharacterController>().controllerPlayer)
        {
            if (c.CompareTag("Placa"))
            {
                hud.interable(true, "Ler", null);
                info = true;
                activeInterable(c);
            }

            if (c.CompareTag("Fruta"))
            {
                hud.interable(true, "Pegar", null);
                activeInterable(c);
            }

            if (c.CompareTag("Door"))
            {
				if (c.GetComponent<DoorInterable> ().podeAbrir) {
					if (c.GetComponent<DoorInterable> ().abrir)
						hud.interable (true, "Fechar", null);
					else
						hud.interable (true, "Abrir", null);
					activeInterable (c);
				} else {
					hud.interable (true,"Trancado", null);
				}
            }

            if(c.CompareTag("NPC")) {
                hud.interable(true, "Falar", null);
                activeInterable(c);
            }
        }
    }

    private void activeInterable(Collider c)
    {
        interable = true;
        this.objColl = c;
    }

    private void OnTriggerExit(Collider other)
    {
        hud.interable(false);
        interable = false;
        objColl = null;
        if(hud.dialogVisible())
        {
            VerificaDialogo();
        }
    }
}
