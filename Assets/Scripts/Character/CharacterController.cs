using System.Collections;
using System.Collections.Generic;
using UnityEngine;
[RequireComponent(typeof(Rigidbody))]
[RequireComponent(typeof(Animator))]
public class CharacterController : MonoBehaviour
{
    [Header("Dados do character")]
    public PlayerTable player;
    public bool controllerPlayer = false;
	public bool perseguirPlayer = false;
    public Transform head;

    [Header("Colissão com o chão")]
    public Transform ground;
    public LayerMask CollisionLayer = -1;

    [Header("Inteligência artificial")]
    public float distanciaMinima;
    public float distanciaMaxima;
    float distancePlayer = 10f;
    public float delayVel = 350;
    public Transform lookAt;

    private Animator anim;

    private bool isJump = false;
    private Rigidbody rgbd;

	public Transform targetCharacter;
    float angle;
    float turnSpeed = 10;
    Vector2 input;
    Quaternion targetPosition;
    HUDController hud;
    GameData gd;

    private Transform cam;
    void Start()
    {
        rgbd = GetComponent<Rigidbody>();
        anim = GetComponent<Animator>();
        cam = Camera.main.transform;
        hud = GameObject.FindGameObjectWithTag("HUD").GetComponent<HUDController>();
        gd = GameObject.Find("GameData").GetComponent<GameData>();

    }
    
    private void FixedUpdate()
    {
        if (chaoCheck())
        {
			if (controllerPlayer)
            {
                input.x = Input.GetAxis("Horizontal");
                input.y = Input.GetAxis("Vertical");

                isJump = false;

                move();
                Jump();
                GerenciarIventario();

                GetComponentInChildren<InterableCharacter>().enabled = true;
            } else
			{
				if (perseguirPlayer) {
					GetComponentInChildren<InterableCharacter> ().enabled = false;
					IA ();
				}
            }
        }
    }

    //Função para verificar se pode andar
    private bool chaoCheck()
    {
        Debug.DrawLine(transform.position, ground.position);
        return Physics.Linecast(transform.position, ground.position, CollisionLayer) ? true : false;
    }

    //Função que faz o personagem andar
    private void move()
    {
        if (input.x != 0 || input.y != 0)
        {
            rgbd.velocity = new Vector3(input.x * player.Speed, 0, input.y * player.Speed) * Time.deltaTime;
            CalculateRotation();
            rotate();
        }

        statusAnimateMove();
    }

    private void statusAnimateMove()
    {
        if (rgbd.velocity != Vector3.zero)
        {
            anim.SetFloat("Walk", 1);
        }
        else
        {
            anim.SetFloat("Walk", 0);
        }
    }

    //Função para calcular a rotação do personagem
    private void CalculateRotation()
    {
        angle = Mathf.Atan2(input.x, input.y);
        angle = Mathf.Rad2Deg * angle;
    }

    //Função quee rotaciona o personagem
    private void rotate()
    {
        targetPosition = Quaternion.Euler(0, angle, 0);
        transform.rotation = Quaternion.Slerp(transform.rotation, targetPosition, turnSpeed * Time.deltaTime);
    }

    //Função que faz o personagem pular
    private void Jump()
    {
        if (Input.GetButtonDown("Jump") && !isJump)
        {
            anim.SetTrigger("Jump");
            rgbd.AddForce(transform.up * player.Jump, ForceMode.Impulse);
            isJump = true;
        }
    }



    private void IA()
    {
        Debug.DrawLine(transform.position, gd.characterAtual().transform.position);
        distancePlayer = Vector3.Distance(transform.position, gd.characterAtual().transform.position);

        if (distancePlayer > distanciaMinima)
        {
			Vector3 rotation = new Vector3(0, gd.characterAtual().transform.rotation.y, 0);
            transform.LookAt(gd.characterAtual().transform);
			/*LocalPosition l = gd.characterAtual ().GetComponent<LocalPosition> ();

			for (int i = 1; i <= l.ocupado.Length; i++) {
				if (!l.ocupado [i]) {
					targetCharacter = l.referencesPosition [i];
					l.ocupado[i] = true;
					break;
				}
			}*/

			//Vector3 rotation = new Vector3(0, targetCharacter.rotation.y, 0);
			//transform.LookAt(targetCharacter);

            rgbd.velocity = transform.forward * (player.Speed - delayVel) * Time.deltaTime;
            move();
        } else
        {
            rgbd.velocity = Vector3.zero;
            input.x = 0;
            move();
        }
    }

    private void GerenciarIventario()
    {
        if(Input.GetButtonDown("Fire3"))
        {
            if(!hud.inventoryActive())
            {
                hud.inventory(true);
            } else
            {
                hud.inventory(false);
            }
        }
    }
}
