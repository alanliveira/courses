using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class CameraController : MonoBehaviour {

    [SerializeField] private Transform lookAt;
    [SerializeField] private float distance = 10.0f;
    [SerializeField] private float duracaoRotacao = 2f;
    [SerializeField] private LayerMask layerColision = -1;

    [SerializeField] private bool limitY = true;
    [SerializeField] private float yAngleMin = 0.0f;
    [SerializeField] private float yAngleMax = 50;

    [SerializeField] private bool limitX = false;
    [SerializeField] private float xAngleMin = 0.0f;
    [SerializeField] private float xAngleMax = 50;
    
    private Transform camTransform;
    private Camera cam;

    private GameObject player;
    private GameData gd;

    private float currentX = 0.0f;
    private float currentY = 0.0f;
    [Range(0, 10)] public float sentivityX = 4.0f;
    [Range(0, 10)] public float sentivityY = 1.0f;

	// Use this for initialization
	void Start () {
        gd = GameObject.Find("GameData").GetComponent<GameData>();
        LookAtHead();

        player = GameObject.FindGameObjectWithTag("Player");
        camTransform = transform;
        cam = Camera.main; // Pega a câmera principal do jogo
	}
	
	// Update is called once per frame
	void Update () {
        LookAtHead();

        //Pegando os ponteiros do mouse
        currentX += Input.GetAxis("Mouse X") * sentivityX;
        currentY += Input.GetAxis("Mouse Y") * sentivityY;

        //Criando um limite para a movimentação da câmera
        if (limitX) currentX = Mathf.Clamp(currentX, xAngleMin, xAngleMax);
        if (limitY) currentY = Mathf.Clamp(currentY, yAngleMin, yAngleMax);
    }
    
    private void LookAtHead()
    {
        lookAt = gd.characterAtual().head;
    }

    void LateUpdate()
    {
        Vector3 dir = new Vector3(0, 0, -distance);//Definindo uma posição para a cÂmera
        Quaternion rotation = Quaternion.Euler(currentY, currentX, 0); //Alterando a rotação da câmera
        
        camTransform.position = lookAt.position + rotation * dir;//Atribuindo a nova poscisão da câmera
        camTransform.LookAt(lookAt.position);
    }
}
