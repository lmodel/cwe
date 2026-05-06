package None;

/* metamodel_version: 1.7.0 */
/* version: 7.3 */
import java.util.List;
import lombok.*;

/**
  Guidance for when and whether to map an issue to a CWE entry (MappingNotesType in XSD). Required on every Weakness, Category, and View.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class MappingNotes  {

  private String usage;
  private String rationale;
  private String comments;
  private List<String> reasons;
  private List<MappingSuggestion> suggestions;

}