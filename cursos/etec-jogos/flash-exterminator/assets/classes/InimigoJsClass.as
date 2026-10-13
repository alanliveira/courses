package classes {
	
	import flash.display.MovieClip;
	
	import flash.display.MovieClip;
	import flash.events.Event;
	import flash.display.Sprite;
	
	public class InimigoJsClass extends MovieClip {
		
		private var nucleo:Object;
		private var vely:Number = 7;
		
		public function InimigoJsClass() {
			// constructor code
			addEventListener(Event.ADDED_TO_STAGE, quandoAdicionado);
		}
		
		private function quandoAdicionado(event:Event):void
		{
			//Acessar a classe principal do jogo
			nucleo = Sprite(root);
			addEventListener(Event.ENTER_FRAME, recarregar);
		}

		private function recarregar(event:Event):void
		{
			//Direção do personagem na tela
			x -=  vely;

			var player:MovieClip = nucleo.nave;

			if(hitTestObject(player)) {
				nucleo.removeChild(player);
				nucleo.gameOver = true;
			}

			for (var i = 0; i < nucleo.tiros.numChildren; i++)
			{
				var atingido:MovieClip = nucleo.tiros.getChildAt(i);
				if (hitTestObject(atingido))
				{
					nucleo.tiros.removeChildAt(i);
					//nucleo.inimigosContainer.removeChild(atingido);
					removeEventListener(Event.ENTER_FRAME, recarregar);
					
					var explodir:MovieClip = new ExplosaoClass();
					
					explodir.x = x;
					explodir.y = y;
					stage.addChild(explodir);
					
					nucleo.inimigoMorto(50);
					nucleo.inimigosContainer.removeChild(this);
					break;
				}
			}
		}
	}
	
}
