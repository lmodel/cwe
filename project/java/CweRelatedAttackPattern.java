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
  A pointer from a weakness to an attack pattern in the CAPEC list.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CweRelatedAttackPattern  {

  private String cAPECID;


}