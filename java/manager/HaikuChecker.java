import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class HaikuChecker
{
		protected HashMap<String,Integer> syllableMap = new HashMap();

		protected static final Pattern[] SubtractSyllables = new Pattern[]
		{
			Pattern.compile("ives"),
			Pattern.compile( "cial"),
			Pattern.compile( "tia"),
			Pattern.compile( "cius"),
			Pattern.compile( "cious"),
			Pattern.compile( "giu"),
			Pattern.compile( "[^aeiouy]ion"),
			Pattern.compile( "iou"),
			Pattern.compile( "sia$"),
			Pattern.compile( ".ely$"),
			Pattern.compile( ".ole."),
			Pattern.compile( "wire"),
			Pattern.compile( "ware."),
			Pattern.compile( "edge[^rad]"),
			Pattern.compile( "(.[aeiouy][^aeiouy][^aeiouy])ed$" ),
			Pattern.compile( "(.[aeiouy][^aeiouytd])ed$" ),
		};

	protected static final Pattern[] AddSyllables = new Pattern[]
		{
			Pattern.compile( "ia" ),
			Pattern.compile( "riet" ),
			Pattern.compile( "dien" ),
			Pattern.compile( "iu" ),
			Pattern.compile( "io" ),
			Pattern.compile( "ii" ),
			Pattern.compile( "[aeiouym]bl$" ),
			Pattern.compile( "[aeiou]{3}" ),
			Pattern.compile( "^mc" ),
			Pattern.compile( "([^aeiouy])le$") ,
			Pattern.compile( "[^l]lien" ) ,	
			Pattern.compile( "^coa[dglx]."),
			Pattern.compile( "[^gq]ua[^auieo]"),
			Pattern.compile( "dnt$" ),
			Pattern.compile( "ier$" ),
			Pattern.compile( "iest$" ),
			Pattern.compile( ".ying$" ),
			Pattern.compile( "oing$" ),
			Pattern.compile( "ie$" ),
			Pattern.compile( "oever$" ),
			Pattern.compile( ".lded$" ),
			Pattern.compile( ".[auieo][^auieo]ted$"),
		};

	public HaikuChecker()
	{
		//HashMap<String,Integer> syllableMap = new HashMap();
		Scanner sc = null;
		try {
			sc = new Scanner(new File("C:\\Users\\MrBrixican\\workspace\\Syllables\\src\\Syllables.txt"));
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		ArrayList<String> words = new ArrayList();
		while(sc.hasNextLine())
		{
			String temp;
			temp = sc.nextLine();
			String key = temp.split("=")[0];
			key=key.toLowerCase().replaceAll("[^a-z]", "");
			int value = temp.split("=")[1].split("·").length;
			if(!syllableMap.containsKey(key))
			{
				syllableMap.put(key,value);
				//words.add(key);
			}
			else{
				if(value!=syllableMap.get(key))
				{
					System.out.println("****WARNING****Inconsistency in dictionary: "+key);
				}
				
			}
			
		}
		sc.close();
		Scanner sc2 = null;
		try {
			sc2 = new Scanner(new File("C:\\Users\\MrBrixican\\workspace\\Syllables\\src\\SyllablesEnhanced.txt"));
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		while(!sc2.hasNextLine())
		{
			
			String temp;
			temp = sc2.nextLine();System.out.println(temp);
			String key = temp;
			key=key.toLowerCase().replaceAll("[^a-z]", "");
			temp=temp.replaceAll("[ Â]", "");
			temp=temp.toLowerCase().replaceAll("[^a-z]", "¥");
			int value = temp.split("¥").length;
			if(!syllableMap.containsKey(key))
			{
				syllableMap.put(key,value);
				//words.add(key);
			}
			else{
				if(value!=syllableMap.get(key))
				{
					//System.out.println("****WARNING****Inconsistency in dictionary: "+key+value+temp);
				}
				
			}
			
		}
		sc2.close();
		//System.out.println(syllableMap.toString());
		//System.out.println(words.size()+", "+words.get(words.size()));
	}
	
	public ArrayList<String> haikuCheck(String lyrics)
	{
		ArrayList<String> haikus = new ArrayList();
		String lyricstemp[]=lyrics.split("[\\r\\n]+");
		for(int i=0;i<lyricstemp.length-2;i++)
		{
			System.out.println(lyricstemp[i+2]);
			if(lineCheck(lyricstemp[i],5)&&lineCheck(lyricstemp[i+1],7)&&lineCheck(lyricstemp[i+2],5))
				haikus.add(lyricstemp[i]+"\n"+lyricstemp[i+1]+"\n"+lyricstemp[i+2]+"\n");
		}
		return haikus;
		
	}
	
	public boolean lineCheck(String line, int sct)
	{
		String linetemp[]=line.split(" ");
		int scounter=0;
		for(int i=0;i<linetemp.length;i++)
		{
			linetemp[i] = linetemp[i].toLowerCase().replaceAll("[^a-z]", "");
			scounter+=countSyllables(linetemp[i]);
			//System.out.println(countSyllables(linetemp[i]));
		}
		//System.out.println(scounter);
		if(scounter==sct)
			return true;
		return false;
	}

	public int countSyllables( String word )
	{
		if(!( ( word == null ) || ( word.length() == 0 ) )&&syllableMap.containsKey(word))
			return syllableMap.get(word);
		//System.out.println(syllableMap.toString());
		int result = 0;
		if ( ( word == null ) || ( word.length() == 0 ) )
		{
			return result;
		}
		String lcWord	= word.toLowerCase();

		lcWord	= lcWord.replaceAll( "'" , "" );

		String[] vowelGroups	= lcWord.split( "[^aeiouy]+" );

		if(lcWord.charAt(lcWord.length()-1)=='e')
			result--;

			for ( Pattern p : SubtractSyllables )
			{
				Matcher m	= p.matcher( lcWord );

				if ( m.find() )
				{
					result--;
				}
			}

			for ( Pattern p : AddSyllables )
			{
				Matcher m	= p.matcher( lcWord );

 				if ( m.find() )
				{
					result++;
				}
			}

			

			if	(	( vowelGroups.length > 0 ) &&
					( vowelGroups[ 0 ].length() == 0 )
				)
			{
				result	+= vowelGroups.length - 1;
			}
			else
			{
				result	+= vowelGroups.length;
			}
			if ( lcWord.length() == 1 )
			{
				result=1;
			}
			syllableMap.put(word,Math.max( result , 1 ));
			System.out.println("Word '"+word+ "' was added to dicitionary with syllable count of "+Math.max( result , 1 )+".");
			return Math.max( result , 1 );
	}
}


