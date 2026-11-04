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
  A link from a weakness to another weakness, in one view.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CweRelatedWeakness  {

  private String nature;
  private CweWeakness cWEID;
  private CweView viewID;
  private CweWeakness chainID;
  private String ordinal;
  private List<CweDimension> dimensions;


}