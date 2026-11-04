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
  One way of preventing a weakness or reducing what it can do.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CweMitigation  {

  private String mitigationID;
  private List<String> phase;
  private List<CweCustomPhase> customPhase;
  private String strategy;
  private String description;
  private String effectiveness;
  private String effectivenessNotes;


}