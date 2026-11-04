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
  A way of looking at the catalogue, as a subset of its entries seen from one standpoint.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CweView extends CweEntry {

  private String type;
  private String objective;
  private List<CweStakeholder> audience;
  private CweRelationships members;
  private String filter;


}