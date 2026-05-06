package None;

/* metamodel_version: 1.7.0 */
/* version: 7.3 */
import java.util.List;
import lombok.*;

/**
  Canonical CWE weakness record (WeaknessType in XSD). Describes a specific type of weakness and the full set of associated information.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Weakness  {

  private int id;
  private String name;
  private String description;
  private String extendedDescription;
  private String abstraction;
  private String structure;
  private String status;
  private String diagram;
  private List<WeaknessOrdinality> weaknessOrdinalities;
  private ApplicablePlatforms applicablePlatforms;
  private List<String> backgroundDetails;
  private List<AlternateTerm> alternateTerms;
  private List<ModeOfIntroduction> modesOfIntroduction;
  private List<String> exploitationFactors;
  private String likelihoodOfExploit;
  private List<CommonConsequence> commonConsequences;
  private List<DetectionMethod> detectionMethods;
  private List<PotentialMitigation> potentialMitigations;
  private List<DemonstrativeExample> demonstrativeExamples;
  private List<ObservedExample> observedExamples;
  private List<String> functionalAreas;
  private List<String> affectedResources;
  private List<TaxonomyMapping> taxonomyMappings;
  private List<Integer> relatedAttackPatterns;
  private List<RelatedWeakness> relatedWeaknesses;
  private List<CWEReference> references;
  private MappingNotes mappingNotes;
  private List<Note> notes;
  private ContentHistory contentHistory;
  private List<String> tags;
  private String source;

}