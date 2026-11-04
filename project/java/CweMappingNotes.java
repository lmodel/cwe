package example;

/* metamodel_version: 1.12.0 */
/* version: 5.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  Guidance on whether to map a real vulnerability to an entry, and on what to use instead.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CweMappingNotes  {

  private String usage;
  private String rationale;
  private String comments;
  private List<CweMappingReason> reasons;
  private List<CweMappingSuggestion> suggestions;


}