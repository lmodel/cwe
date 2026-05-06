package None;

/* metamodel_version: 1.7.0 */
/* version: 7.3 */
import java.util.List;
import lombok.*;

/**
  A suggested alternative CWE entry for mapping purposes (SuggestionsType/Suggestion in XSD).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class MappingSuggestion  {

  private int cweId;
  private String comment;

}