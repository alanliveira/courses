package  {
	import flash.display.MovieClip;
	import flash.events.Event;
	
	public class tiroClip extends MovieClip{
		var larguraTela:Number;
		var alturaTela:Number;
		
		//criando duas constante da classe
		const direcao:int = 10;
		const foraTela:int = -10;
		
		//função construtora da classe
		public function tiroClip() {
			// constructor da classe
			this.addEventListener(Event.ADDED_TO_STAGE, quandoAdd);
		}
		
		private function quandoAdd(event:Event):void {
			larguraTela = stage.width;
			alturaTela = stage.height;
			addEventListener(Event.ENTER_FRAME, recarregar);
		}
		
		private function recarregar(event:Event):void {
			if (y < foraTela) {
				removeEventListener(Event.ENTER_FRAME, recarregar);
				parent.removeChild(this);
			}
				x += direcao;
		}
	}
}
