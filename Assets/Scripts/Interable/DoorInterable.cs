using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DoorInterable : MonoBehaviour {

    public enum ModoAbrir
    {
        rotacao, lateral
    }

    public ModoAbrir modoAbertura = ModoAbrir.rotacao;

    public Transform target;

    public bool podeAbrir = false;
    public bool abrir = false;

    public Animator anim;

    // Use this for initialization
    void Start()
    {
        anim = target.GetComponent<Animator>();
    }

    private void Update()
    {
        switch (modoAbertura)
        {
            case ModoAbrir.rotacao:
                if(abrir)
                {
                    anim.SetBool("rotate", true);
                } else
                {
                    anim.SetBool("rotate", false);
                }
                break;
            case ModoAbrir.lateral:
                if (abrir)
                {
                    anim.SetBool("move", true);
                }
                else
                {
                    anim.SetBool("move", false);
                }
                break;
        }
    }
}
