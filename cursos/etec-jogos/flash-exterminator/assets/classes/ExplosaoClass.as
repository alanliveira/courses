package classes
{

	import flash.display.MovieClip;
	import flash.display.MovieClip;
	import flash.events.Event;
	import flash.media.Sound;

	public class ExplosaoClass extends MovieClip
	{
		private var explodir:Sound = new sfxExplosao();
		
		public function ExplosaoClass()
		{
			// constructor code
			addEventListener(Event.ENTER_FRAME, inimigoMorto);
			explodir.play();
		}

		private function inimigoMorto(event:Event):void
		{
			if (currentFrame == framesLoaded)
			{
				removeEventListener(Event.ENTER_FRAME, inimigoMorto);
				parent.removeChild(this);
			}
		}
	}
}